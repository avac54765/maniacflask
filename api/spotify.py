# API calls to Spotify Rest API
# RESEARCH & WORK ON ACCESS TOKEN

# Spotify Info <- use this it's literally amazing: https://developer.spotify.com/documentation/web-api
# ^ Provides much more options (top artists songs, related albums, etc) 
# different format options (curl, wget, httpie)

#If using wget need specific format to work in python file
import requests

url = 'https://api.spotify.com/v1/search?q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis&type=album'
headers = {'Authorization': 'Bearer BQA-zn...kBCGh9'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    content = response.text
    print(content)
else:
    print('Request failed with status code:', response.status_code)


# GET Album
url = 'https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy'
headers = {'Authorization': 'Bearer BQA-zn...kBCGh9'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    content = response.text
    print(content)
else:
    print('Request failed with status code:', response.status_code)


wget --quiet \
  --method GET \
  --header 'Authorization: Bearer BQDT1E...x4Phso' \
  --output-document \


# GET Artist
wget --quiet \
  --method GET \
  --header 'Authorization: Bearer BQALbP...DSPCOf' \
  --output-document \
  - https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg


# SEARCH!! (basically GET song)
url = 'https://api.spotify.com/v1/search?q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis&type=album'
headers = {'Authorization': 'Bearer BQA-zn...kBCGh9'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    content = response.text
    print(content)
else:
    print('Request failed with status code:', response.status_code)