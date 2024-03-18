### OBS ###
###
### API bör köras tidigast 13:30 annars är priserna inte satta för efterkommande dag
###
### OBS ###

from http.client import responses
import requests
import http
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from dotenv import load_dotenv
import os
from pathlib import Path
import datetime
import sys



### datetime ###
Current_Date = datetime.datetime.today()
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
TomorrowRateStart = NextDay_Date.replace(hour=0, minute=0,second=0,microsecond=0).isoformat('T')
TomorrowRateEnd = NextDay_Date.replace(hour=23, minute=59, second=59, microsecond=0).isoformat('T')
startTime = str(TomorrowRateStart) + "Z" # Format - date-time (as date-time in RFC3339). Used to select content for a given start time in UTC, with a special UTC designator('Z'). e.g. 2019-05-30T23:59:59Z
endTime = str(TomorrowRateEnd) + "Z" # Format - date-time (as date-time in RFC3339). Used to select content for a given end time in UTC, with a special UTC designator('Z'). e.g. 2019-05-30T23:59:59Z

### datetime ###

#######################
dotenv_path = Path(r'nordpool.env') # replace with the actual path tolink to env file
load_dotenv(dotenv_path=dotenv_path)

password = os.getenv('password')
user_name = os.getenv('user_name')
api_key= os.getenv('api_key')
token_url= os.getenv('auth_url')
dayahead_url = os.getenv('dayahead_url')
host = os.getenv('host')
authorization="Basic "+ str(api_key)
scope=os.getenv('scope')

### Authorization ###
headers = {
    "Authorization": authorization,
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "grant_type": "password",
    "scope": scope,
    "username": user_name,
    "password": password
}

response = requests.post(token_url, headers=headers, data=payload, verify=False)
response_code = response.status_code
print("Authorization Response Code:", response_code)
jsonResponse = json.loads(response.text)
access_token = jsonResponse['access_token']
# print(access_token)

## Authorization ###


### Market Data - Day Ahead AreaPrices ###
deliveryarea = "SE3" # Used to filter content by area code (e.g. NO1, NO2, SE1, SE2, FI)
currency = "SEK" # Used to filter content by currency code (e.g. EUR, NOK, SEK)
# startTime = "2024-03-13T00:00:00Z" #Format - date-time (as date-time in RFC3339). Used to select content for a given start time in UTC, with a special UTC designator('Z'). e.g. 2019-05-30T23:59:59Z
# endTime = "2024-03-13T23:59:59Z" #Format - date-time (as date-time in RFC3339). Used to select content for a given end time in UTC, with a special UTC designator('Z'). e.g. 2019-05-30T23:59:59Z
authorization_key= "Bearer " + access_token

headers = {
    "Host": host,
    "accept": "application/json",
    "Authorization": authorization_key
}

headers = {
    "Host": host,
    "accept": "application/json",
    "Authorization": authorization_key
}

params = {
    "currency": currency,
    "startTime": startTime,
    "endTime": endTime,
    "deliveryarea": deliveryarea,
    "status": "O",
    "scope": scope
}

response = requests.get(dayahead_url, headers=headers, params=params)

# Parse the response JSON to extract the access token
jsonResponse = response.json()
response_code = response.status_code
print("Request Response Code:", response_code)
# print(jsonResponse)