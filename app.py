from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


CARS = [
   {
      'id':1,
      'title': 'Porche GT3 RS',
      'location': 'Toronto, ON',
      'price': 230000

   },

   {
      'id':2,
      'title': 'Mercades AMG',
      'location': 'Addis Abeba, Ethiopia',
      'price': 150000

   },

   {
      'id':3,
      'title': 'Toyota GR86',
      'location': 'Aden, Yemen',
      'price': 30000

   }
]



@app.route("/")
def hello_world():
    return render_template('home.html', cars=CARS)

@app.route("/api/cars")
def list_cars():
  return jsonify(CARS)


if __name__== "__main__":
  app.run(debug=True)