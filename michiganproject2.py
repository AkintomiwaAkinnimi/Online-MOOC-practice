import requests_with_caching
import json

def get_movies_from_tastedive(query):
    baseurl = "https://tastedive.com/api/similar"
    params = {}
    params['limit'] = 5
    params['type'] = "movies"
    params['q'] = query
    x = requests_with_caching.get(baseurl, params)
    return x.json()


def extract_movie_titles(movie):
    movie_titles = []
    for i in range(len(movie['Similar']['Results'])):
        movie_titles.append(movie['Similar']['Results'][i]['Name'])
    return movie_titles

def get_related_titles(lst):
    final_list = []
    for item in lst:
        y = extract_movie_titles(get_movies_from_tastedive(item))
        for movie in y:
            if movie not in final_list:
                final_list.append(movie)
    return final_list

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    params = {}
    params['t'] = title
    params['r'] = "json"
    x = requests_with_caching.get(baseurl, params=params)
    return x.json()

def get_movie_rating(movie):
    for item in movie['Ratings']:
        if item['Source'] == "Rotten Tomatoes":
            return int(item['Value'][:-1])
    return 0

def get_sorted_recommendations(lst):
    rel = get_related_titles(lst)
    sorted_rel = sorted(rel, key=lambda title: (get_movie_rating(get_movie_data(title)), title), reverse=True)
    return sorted_rel
