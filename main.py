import os
from dotenv import load_dotenv
import requests

load_dotenv()

client_id = os.getenv('AMADEUS_CLIENT_ID')
client_secret = os.getenv('AMADEUS_CLIENT_SECRET')

token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    ## access_token = response.json().get('access_token') # Extracting access token
    token_state = response.json().get('state') # Extracting token state
    print("Token State:", token_state) 
   ## print("Access Token:", access_token)
    
else:
    print("Failed to retrieve access token")
    exit()