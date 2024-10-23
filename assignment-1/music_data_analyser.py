import json



with open('assignment-1/database/spotify.json', mode= 'r') as artist_data:
    data = json.load(artist_data)
    items = data['items']
    previous = data['next']

    print(data.values())
    
    artist_name = items[0]['artists'][0]['name']
    print(f"{artist_name:.>5}")

    for i in range(0, 20):
        number_of_tracks_in_album = items[i]['total_tracks']
        artist_name = items[i]['artists'][0]['name']
        album_name = items[i]['name']
        print(f"Album: \t{album_name:.^4}\n Tracks: {number_of_tracks_in_album:}")


