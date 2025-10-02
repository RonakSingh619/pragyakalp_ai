import requests

api_url = "http://localhost:21465/sendMessage"
payload = {
    "phone": "+919834001393",  # Replace with recipient number
    "message": "Hello from my personal WhatsApp!"
}

response = requests.post(api_url, json=payload)
print(response.json())