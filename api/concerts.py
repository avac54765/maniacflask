# events request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/events/MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0"

headers = {
    "X-RapidAPI-Key": "MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())




# venues request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/venues/MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0"

headers = {
	"X-RapidAPI-Key": "MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())



# performers request
import requests

url = "https://seatgeek-seatgeekcom.p.rapidapi.com/performers/MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0"

headers = {
	"X-RapidAPI-Key": "MzM3NjkyNzh8MTY4NDM5NTczMC41NTQyODI0",
	"X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())