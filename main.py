import requests
api_url = "https://corporatebs-generator.sameerkumar.website/"
response = requests.get(api_url)
print(response.json())