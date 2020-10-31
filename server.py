from flask import Flask, render_template
import view

from database import Database
from movies import Movie


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/",view_func=view.home_page)
    app.add_url_rule("/movies", view_func=view.movies_page)
    app.add_url_rule("/movies/<int:movie_key>", view_func=view.movie_page)
    app.add_url_rule("/auth/<string:types>",view_func=view.auth_page)
    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five", year=1972))
    db.add_movie(Movie("The Shining"))
    app.config["db"] = db
    app.config['templates_auto_reload'] = True


    app.config.from_object("settings")
    return app



if __name__ == "__main__":
    app = create_app()
    app.run(host="localhost", port=8000)
