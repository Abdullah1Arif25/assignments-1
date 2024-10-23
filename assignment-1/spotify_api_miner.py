import requests
import json
import requests
import json
import re


service = 'https://dit009-spotify-assignment.vercel.app/api/v1/'


def by_artist_id():
    artist_link = input(""" Enter the links of the artists: """)
    ids = re.findall(r'\d\w{21}', artist_link)


    for artist_id in ids:
        url = f"{service}/artists/{artist_id}/albums"

        response = requests.get(url)

        data = response.json()

        with open('assignment-1/database/spotify.json', mode = 'a') as spotify_file:
            json.dump(data, spotify_file)





def by_artist_name():

    artist_name = input("Enter a name of the artist: ").strip().lower()

    url = f"{service}/search?q={artist_name}&type=album"
    response = requests.get(url)
    data = response.json()

    with open("assignment-1/database/specific_artist.json", mode = 'a') as specific_artist:
        json.dump(data, specific_artist )




def main():
    data_option = int(input("""
    Select an Option:
        1. Import Data by Urls.
        2. Import Data By Name.
        """))
    if data_option  == 1:
        by_artist_id()
    else:
        by_artist_name


if __name__ == "__main__":
    main()







