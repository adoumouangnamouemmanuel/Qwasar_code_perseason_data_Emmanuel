#
#
#PART1
#using flask
#route GET on /
#
#Open the csv
#search for Genre
#
#

#
#Access parse
#return json

from flask import Flask, request
import csv
import json

app = Flask(__name__)


def movie_filter(genre):
    result = []
    filename = "imdb-movie-data.csv"
        

    with open(filename) as csvfile:
        csv_content = csv.DictReader(csvfile)

        for movie in csv_content:
            genres = movie["Genre"].split(",")
            if genre in genres:
                result.append(movie)

    return json.dumps(result)

@app.route("/")
def root():
    print(request.args.get("genre"))
    my_list = movie_filter(request.args.get("genre").title())
    return my_list
   

@app.route("/action")
def data():
    #print(request.args.get("genre"))
    return movie_filter("Action")

@app.route("/adventure")
def data_adventure():
    return movie_filter("Adventure")
    

@app.route("/comedy")
def data_comedy():
    return movie_filter("Comedy")
    

@app.route("/drama")
def data_drama():
    return movie_filter("Drama")

@app.route("/romance")
def data_romance():
    return movie_filter("Romance")



app.run("0.0.0.0", port=8080)
