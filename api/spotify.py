# API calls to Spotify Rest API
# RESEARCH & WORK ON ACCESS TOKEN

# Spotify Info <- use this it's literally amazing: https://developer.spotify.com/documentation/web-api

# GET Album
wget --quiet \
  --method GET \
  --header 'Authorization: Bearer BQDT1E...x4Phso' \
  --output-document \
  - https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy


# GET Artist
wget --quiet \
  --method GET \
  --header 'Authorization: Bearer BQALbP...DSPCOf' \
  --output-document \
  - https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg

