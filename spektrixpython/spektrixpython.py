from requests import Request, Session
from json import dumps
from json.decoder import JSONDecodeError
from datetime import datetime
from hashlib import sha1, md5
import hmac
from base64 import b64encode, b64decode


class SpektrixCredentials(object):

    def __init__(self, client_name, api_user, api_key):
        self.client_name = client_name
        self.api_user = api_user
        self.api_key = api_key


class SpektrixRequest(object):

    def __init__(self, endpoint, credentials):

        self.spektrix_api_user = credentials.api_user
        self.spektrix_api_key = credentials.api_key

        base_url = "https://system.spektrix.com/" + credentials.client_name + "/api/v3/"
        self.url = base_url + endpoint

    def get(self):
        self.method = "GET"
        response = self._make_request()
        return response

    def post(self, payload=None):
        self.method = "POST"
        response = self._make_request(payload)
        return response

    def patch(self, payload):
        self.method = "PATCH"
        response = self._make_request(payload)
        return response

    def put(self, payload):
        self.method = "PUT"
        response = self._make_request(payload)
        return response

    def delete(self, payload=None):
        self.method = "DELETE"
        response = self._make_request(payload)
        return response

    def _generate_auth_headers(self, payload=None):
        date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

        string_to_sign = self.method + "\n" + self.url + "\n" + date

        if self.method != "GET":
            body_string = dumps(payload).encode("utf-8")
            body_string = md5(body_string).digest()
            body_string = str(b64encode(body_string), "utf-8")

            string_to_sign = string_to_sign + "\n" + body_string

        decoded_key = b64decode(self.spektrix_api_key)
        string_to_sign = string_to_sign.encode("utf-8")

        signature = hmac.new(decoded_key, string_to_sign, sha1).digest()
        signature = b64encode(signature).decode("utf-8")

        headers = {}
        headers["Date"] = date
        headers["Authorization"] = "SpektrixAPI3 {}:{}".format(
            self.spektrix_api_user, signature
        )

        return headers

    def _make_request(self, payload=None):

        if payload == None:
            # Spektrix assumes any non-GET request must have a body.
            payload = {}
        else:
            payload = [payload]

        headers = self._generate_auth_headers(payload)

        session = Session()
        req = Request(method=self.method, url=self.url, json=payload, headers=headers)

        response = session.send(req.prepare())

        response.raise_for_status()

        try:
            return response.json()
        except JSONDecodeError:
            # There is one endpoint which returns non-JSON content (instances/{}/status/detail)
            return response.content
