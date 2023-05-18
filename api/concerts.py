# events request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/events"

headers = {
	"X-RapidAPI-Key": "7b146afe20msh92e84c02ae27c6ap1185b5jsnb7a574f24cbe",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())




# venues request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/venues"

headers = {
	"X-RapidAPI-Key": "7b146afe20msh92e84c02ae27c6ap1185b5jsnb7a574f24cbe",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())



# performers request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/performers"

headers = {
	"X-RapidAPI-Key": "7b146afe20msh92e84c02ae27c6ap1185b5jsnb7a574f24cbe",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())