import requests
import json
import re


service = 'https://dit009-spotify-assignment.vercel.app/api/v1/'



artist_link = input(""" Enter the link of the artists: """)
ids = re.findall(r'\d\w{21}', artist_link)

for id in ids:
    artist_id = id

    link = f"{service}/artists/{artist_id}/albums"
    
    response = requests.get(link)
    
    data = response.json()
    with open('C:/Users/aa695/go/src/assignment-1/abd.json', 'a') as robiyat:
        json.dump(data, robiyat)





        








