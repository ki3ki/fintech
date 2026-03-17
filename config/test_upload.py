import requests

url = "http://127.0.0.1:8000/api/upload/"

files = {
    "file": open("transactions.csv", "rb")
}

response = requests.post(url, files=files)

print(response.json())