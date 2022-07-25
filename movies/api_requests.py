import requests
from decouple import config

API_KEY= config('API_KEY')

# GETTING LIST BY Trending
def get_trending():
    response = requests.get(f'https://api.themoviedb.org/3/trending/all/day?api_key={API_KEY}')
    return response.json()

# GETTING LIST BY Top Rated
def get_top_rated():
    response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}')
    return response.json()

# GETTING LIST BY GENRE
def get_genre(genre_id):
    response = requests.get(f'https://api.themoviedb.org/3/list/{genre_id}?api_key={API_KEY}')
    return response.json()

def get_movie(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}')
    return response.json()

# GETTING THE TRAILER FOR THE MOVIE
def get_video(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}')
    return response.json()

# GETTING THE MOVIE BY SEARCH FUNCTIONALITY
def multi_search(query):
    response = requests.get(f'https://api.themoviedb.org/3/search/multi?query={query}&api_key={API_KEY}&language=en-US&page=1&include_adult=true')
    return response.json()