# spektrixpython
A Python module for interacting with Spektrix API v3. This is module is written by a third party and is not supported by or affiliated with Spektrix.

## Usage

### Installation

`pip install spektrixpython`

### Example

Create a `spektrixpython.ini` config file from the `spektrixpython.ini.sample` template.

```python
from spektrixpython import SpektrixRequest

# Get a list of events
events = SpektrixRequest('events').get()
print events

# Create a new basket and print the Id
basket = SpektrixRequest('baskets').post()
print basket['id']
```

## License

This module is licensed under the MIT License. Please see the LICENSE file for full details.
