# Lomograpy

It's just a simple form to make Lomography API requests easier.


You can get yout API Key [here](<https://api.lomography.com/>)



## Usage Example

<code>

import Lomograpy as lomogracinha

key = 'YOURAPIKEY'


popular_photos = lomograchinha.get_popular_photos(api_key=key)
print(popular_photos)
