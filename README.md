# spektrixpython
A Python module for interacting with Spektrix API v3. This module is written
by a third party and is not supported by or affiliated with Spektrix.

For API v3 documentation, visit `https://system.spektrix.com/<clientname>/api/help`,
replacing `<clientname>` with your Spektrix system name.

## Usage

### Installation

`pip install spektrixpython`

Create a `spektrixpython.ini` config file from the `spektrixpython.ini.sample` template and fill in the details for your Spektrix system.

### Example

```python
from spektrixpython import SpektrixRequest

# Get a list of events
events = SpektrixRequest('events').get()
print events

# Create a new basket
basket = SpektrixRequest('baskets').post()['id']

# Add a merchandise item to the newly created basket
endpoint = 'baskets/{}/merchandise'.format(basket)

# Replace this stockItem Id with one from your Spektrix system.
payload = {'stockItem':'1AHGJDSMMPLMPPGNLJBQVLBRSKVDLQRPP'}

SpektrixRequest(endpoint).post(payload)
```

## License

This module is licensed under the MIT License. Please see the LICENSE file for
full details.
