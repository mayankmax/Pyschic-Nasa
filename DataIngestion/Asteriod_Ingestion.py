import requests

APIKEY = 'v65cdiWTThIq1PV5EB0iQNLpWhBkudafM64gZbyu'

def asteroid():
    # API for retrieving a list of Asteroids based on their closest approach date to Earth
    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2023-12-01&end_date=2023-12-01&api_key={APIKEY}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        api_data = response.json()
        return api_data
    
    else:
        print("Error Generated")



