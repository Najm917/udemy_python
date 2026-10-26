import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = {
    "authorization": "AAPKI_FAST2SMS_API_KEY",
    "message": "It is going to rain today. Please bring an umbrella ☂️",
    "language": "english",
    "route": "q",  # Quick SMS route
    "numbers": "9525792916",  # Aapka mobile number
}

response = requests.get(url, params=payload)
print(response.json())