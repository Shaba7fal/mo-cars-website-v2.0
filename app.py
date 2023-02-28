from flask import Flask, render_template, url_for, jsonify
import pandas as pd
from database import engine, text, load_cars_from_db, load_car_from_db

app = Flask(__name__)



@app.route("/")
def hello_world():
    cars = load_cars_from_db()
    return render_template('home.html', cars=cars)

@app.route("/api/cars")
def list_cars():
  CARS = load_cars_from_db()
  return jsonify(CARS)


@app.route("/car/<id>")
def show_car(id):
   job = load_car_from_db(id)
   return jsonify(job)


if __name__== "__main__":
  app.run(debug=True)