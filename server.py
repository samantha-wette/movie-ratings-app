"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movies')
def view_movies():

    movies = crud.show_all_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie_detail(movie_id):
    
    movie = crud.show_movie_by_id(movie_id)
    # movie = crud.show_all_movies(Movie.query.filter(Movie.movie_id==movie_id))
    return render_template('movie_details.html', movie=movie)
    
@app.route('/users')
def show_all_users():
    users = crud.show_all_users()
    return render_template('all_users.html', users=users)

@app.route('/users', methods=['POST'])
def create_new_user():
    '''Create user profile'''


@app.route('/users/<user_id>')
def show_user_detail(user_id):
    user = crud.show_user_by_id(user_id)
    return render_template('user_details.html', user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

