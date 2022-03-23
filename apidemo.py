import json
import requests
def getinfo (country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    result = requests.get(url)
    data = result.json()
    # print(data,indent =4)
    print(json.dumps(data,indent=4))

    print("-"*50)
    print(f"Country Name = {data[0]['name']['common']}")
    print(f"Capital City = {data[0]['capital'][0]}")
    print(f"Region = {data[0]['region']}")
    print(f"Country Population = {data[0]['population']}")
    
    print("-"*25)


getinfo(input("Enter Country Name:"))
