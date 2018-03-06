# spektrixpython
A Python 3 module for interacting with Spektrix API v3. This module is written
by a third party and is not supported by or affiliated with Spektrix.

For API v3 documentation, visit `https://system.spektrix.com/<clientname>/api/v3/help`,
replacing `<clientname>` with your Spektrix system name.

## Usage

### Installation

`pip install spektrixpython`

### Example

```python
from spektrixpython import SpektrixCredentials, SpektrixRequest


credentials = SpektrixCredentials(client_name="SPEKTRIX CLIENT NAME",
                                  api_user="API USERNAME",
                                  api_key="API KEY")

# Get a list of events
events = SpektrixRequest(endpoint='events', credentials=credentials).get()
print(events)

# Create a new basket
basket = SpektrixRequest(endpoint='baskets', credentials=credentials).post()['id']

# Add a merchandise item to the newly created basket
endpoint = 'baskets/{}/merchandise'.format(basket)

# Replace this stockItem Id with one from your Spektrix system.
payload = {'stockItem':'1AHGJDSMMPLMPPGNLJBQVLBRSKVDLQRPP'}

SpektrixRequest(endpoint=endpoint, credentials=credentials).post(payload)
```

## License

This module is licensed under the MIT License. Please see the LICENSE file for
full details.
