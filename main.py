import requests
import json

api_url = "https://corporatebs-generator.sameerkumar.website/"

print("Need a company motto? We have the solution you've been waiting for!\n")
CompanyName = input("Please enter your company name: ")
print("Here are 10 mottos for " + CompanyName+ ":\n")

for i in range(10):
    FirstResponse = requests.get(api_url)
    FirstPhrase = json.loads(FirstResponse.text)
    SecondResponse = requests.get(api_url)
    SecondPhrase = json.loads(SecondResponse.text)
    print("Here at " + CompanyName + " we " + FirstPhrase["phrase"].lower() + " and " + SecondPhrase["phrase"].lower() + ".")
