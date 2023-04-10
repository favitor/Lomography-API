# Lomograpy

It's just a simple form to make Lomography API requests easier.


You can get yout API Key [here](<https://api.lomography.com/>)



## Usage Example

```python

import Lomograpy as lomogracinha

key = 'YOURAPIKEY'


popular_photos = lomogracinha.get_popular_photos(self_page=2, api_key=key)
print(popular_photos.json())


