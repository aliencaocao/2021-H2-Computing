import json
import pymongo

conn = pymongo.MongoClient('127.0.0.1', 27017)
moviedb = conn['movieDB']
movie_coll = moviedb['movie']
data = [{"Title": "Mortal Kombat", "Year": "2021", "Rated": "R", "Runtime": 110, "Genre": ["Action", "Adventure", "Fantasy"], "Rating": "7"},
        {"Title": "Wrong Turn", "Year": "2021", "Rated": "R", "Runtime": 109, "Genre": ["Horror", "Thriller"], "Rating": "5"},
        {"Title": "The Little Things", "Year": "2021", "Rated": "R", "Runtime": 130, "Genre": ["Crime", "Drama", "Thriller"], "Rating": "6"},
        {"Title": "Barb and Star Go to Vista Del Mar", "Year": "2021", "Rated": "PG-13", "Runtime": 100, "Genre": ["Comedy"], "Rating": "7"},
        {"Title": "Minari", "Year": "2020", "Rated": "PG-13", "Runtime": 115, "Genre": ["Drama"], "Rating": "8"},
        {"Title": "Music", "Year": "2021", "Rated": "PG-13", "Runtime": 110, "Genre": ["Drama", "Musical"], "Rating": "3"},
        {"Title": "Nomadland", "Year": "2020", "Rated": "R", "Runtime": 105, "Genre": ["Drama"], "Rating": "8"},
        {"Title": "Flora & Ulysses", "Year": "2021", "Rated": "PG", "Runtime": 95, "Genre": ["Comedy", "Adventure", "Family"], "Rating": "6"},
        {"Title": "Tom and Jerry", "Year": "2021", "Rated": "PG", "Runtime": 100, "Genre": ["Animation", "Comedy", "Family"], "Rating": "5"},
        {"Title": "The Unholy", "Year": "2021", "Rated": "PG", "Runtime": 99, "Genre": ["Horror"], "Rating": "5"},
        {"Title": "The Courier", "Year": "2020", "Rated": "PG", "Runtime": 112, "Genre": ["Thriller"], "Rating": "7"}]
movie_coll.insert_many(data)
result = movie_coll.find()
for i in result:
    print(i)
conn.close()
