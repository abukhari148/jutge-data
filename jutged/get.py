import requests
from pprint import pprint

URL = "https://jutge.org/problems/{problem}/"
PROBLEM = ""
response = requests.get(URL.format(problem="P10694"))
response.raise_for_status()
pprint(response.text)
