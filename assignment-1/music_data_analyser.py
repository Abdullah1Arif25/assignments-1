import json

with open('assignment-1/database/specific_artist.json', mode= 'r') as artist_data:
    data = json.load(artist_data)
    
tracks = data['tracks']
    
def popular_track():
    
    artist_name = tracks[0]['album']['artists'][0]["name"]
    max_popularity = 0
    popular_track = ""
    

    for i in range(len(tracks)):

        popularity = tracks[i]['popularity']
        
        track_name = tracks[i]['name']
        
        if popularity > max_popularity:
            max_popularity = popularity
            popular_track = track_name
    
    print(f"{artist_name}'s most popular track is {popular_track} with popularity of {max_popularity}.")

def least_track():
    
    artist_name = tracks[0]['album']['artists'][0]["name"]
    least_popularity = 100
    least_track = ""
    

    for i in range(len(tracks)):
        
        popularity = tracks[i]['popularity']
        track_name = tracks[i]['name']
        
        if popularity < least_popularity:
            least_popularity = popularity
            least_track = track_name
    
    print(f"{artist_name}'s least popular prack is {least_track} with a popularity of {least_popularity}.")
   

def related_artists():
    
    with open("assignment-1/database/specific_artist.json", 'r') as Spotify_data:
        
        data = json.load(Spotify_data)

        tracks = data['tracks']
    
    print("The related artists are: ")

    for i in range(len(tracks)):
        current_track = tracks[i]['album']['artists']

        for j in range(len(current_track)):
            related_artist = current_track[j]['name']

            if related_artist == "The Weeknd":
                continue
            
            print(related_artist)

def main():

    user_input = int(input("""
         1. Get Top Track and Popularity.
         2. Get Least Popular Track.
         3. Get Related Aritists. 
        
        Enter Your Option:  """))
    
    if user_input == 1:
        popular_track()
    
    elif user_input == 2:
        least_track()
    
    elif user_input == 3:
        related_artists()
    
    else:
        print("Invalid input. Enter 1, 2 or 3.")
        return main()
    

if __name__ == "__main__":
    main()
