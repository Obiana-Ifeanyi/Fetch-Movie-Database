import requests
import json

API_KEY = '00857a44151942bf78aa56abbc27c7ed'
BASE_URL = 'https://api.themoviedb.org/3/movie/popular'
REQUEST_URL = f'{BASE_URL}?api_key={API_KEY}&language=en-US&page=1'
responses = requests.get(REQUEST_URL)

try:
    if responses.status_code == 200:
        data = responses.json()
        print ('Movies rated by popularity')
        for movies in data['results']:
            movie_titles = movies['original_title']
            release_date = movies['release_date']
            overview = movies['overview']
            rating = movies['vote_average']
            print (f"movie_title: {movie_titles}\noverview: {overview}\nrating: {rating}")
            print (f"release_date: {release_date}\n\n")

    elif responses.status_code == 404:
        print ('404 error')

    else:
        print ('an error just occured')

except:
    pass
