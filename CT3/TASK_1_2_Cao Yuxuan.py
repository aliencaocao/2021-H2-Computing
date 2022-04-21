import pymongo

conn = pymongo.MongoClient('127.0.0.1', 27017)
moviedb = conn['movieDB']
movie_coll = moviedb['movie']


def printAllResults(result):
    for i in result:
        print(f'Title: {i["Title"]}, Year: {i["Year"]}, Rated: {i["Rated"]}, Rating: {i["Rating"]}, Runtime: {i["Runtime"]}')


print('Movies rated PG:')
result = movie_coll.find({'Rated': 'PG'})
printAllResults(result)
print()

print('Movies with Drama genre sorted by descending runtime:')
result = movie_coll.find({'Genre': 'Drama'}).sort('Runtime', pymongo.DESCENDING)
printAllResults(result)
print()

print('Movies with runtime greater than or equal to 95 and less than 110min:')
result = movie_coll.find({'Runtime': {'$gte': 95, '$lt': 110}})
for i in result:
    print(i)
print()

movie_coll.update_many({'$and': [{'Rated': 'PG'}, {'Genre': {'$in': ['Horror', 'Thriller']}}]}, {'$set': {'Rated': 'PG-13'}})
