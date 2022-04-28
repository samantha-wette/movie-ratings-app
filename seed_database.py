"""Script to seed db"""

import os
import json
from random import choice, randint
from datetime import datetime

import model
import server
import crud

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []

for movie in movie_data:

     # 2019-09-20
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    #movies_in_db = [(title, overview, poster_path, release date)]


    # TODO: create a movie here and append it to movies_in_db
    format = "%Y-%m-%d"
    date = datetime.strptime(movie['release_date'], format)
    title, overview, poster_path, date = (movie['title'], movie['overview'],
    movie['poster_path'], movie['release_date'])

    db_movie = crud.create_movie(title, overview, date, poster_path)
    movies_in_db.append(db_movie)

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    new_user = crud.create_user(email, password)
    model.db.session.add(new_user)

    for rating in range(10):
        randommovie = choice(movies_in_db)
        score = randint(1, 5)

        new_rating = crud.create_rating(new_user, randommovie, score)
        model.db.session.add(new_rating)


model.db.session.add_all(movies_in_db)
model.db.session.commit()