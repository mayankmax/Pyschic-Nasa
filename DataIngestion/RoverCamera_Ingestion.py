import requests

APIKEY = 'v65cdiWTThIq1PV5EB0iQNLpWhBkudafM64gZbyu'

def RoverCamera():
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1&page=2&api_key={APIKEY}'
    
    
    response = requests.get(url)
    
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        return response_data
    else:
        return "Error in getting Data from API"
    
    
    

RoverCamera()