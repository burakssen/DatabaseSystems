from flask import Flask, render_template, current_app, abort
from datetime import datetime


def number_of_cards():
    return 5

def home_page():
    burak = [1,2,3,6,7]
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", cards=number_of_cards())

def movies_page():
    db = current_app.config["db"]
    movies = db.get_movies()
    return render_template("movies.html", movies=sorted(movies))

def movie_page(movie_key):
    db = current_app.config["db"]
    movie = db.get_movie(movie_key)
    if movie is None:
        abort(404)
    return render_template("movie.html", movie=movie)

def auth_page(types):
    print(types != "admin")
    if types != "student" and types != "admin":
        abort(404)
    return render_template("authentication.html", type=types)