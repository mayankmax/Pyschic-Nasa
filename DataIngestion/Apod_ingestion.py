import requests

APIKEY = 'v65cdiWTThIq1PV5EB0iQNLpWhBkudafM64gZbyu'

def ApodIngestion():
    
    #API for One of the most popular websites at NASA is the Astronomy Picture of the Day
    url = f'https://api.nasa.gov/planetary/apod?api_key={APIKEY}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        result = response.json()
       # print(result)
        return result
    else:
        return "Error while fetching from API"
    
    
    
    
    
