import requests
import json

def get_covid19_report(url):
    response = requests.get(url)
    data = response.json()
    with open('download/data.json', 'w') as f:
        json.dump(data, f)
    return data

# Pull here...
url = 'https://covid19.th-stat.com/api/open/cases'
get_covid19_report(url)