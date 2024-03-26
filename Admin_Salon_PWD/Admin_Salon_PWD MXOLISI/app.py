
from flask import Flask, render_template, request, url_for, flash 
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:5000/AdminSalon"
Mongo = PyMongo(app)
db = Mongo.db


@app.route('/signup', methods=["POST","GET"])
def signup():
  if request.method =="post":
     salonname = request.form["name"]
     email = request.form["email"]
     address = request.form["address"]
     password = request.form["password"]
     confirm_password = request["Confirm password"]

     salondetails = {salonname:"name"}

     db.AdminSalon.insert_one(salondetails)
     print(salonname)

  return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)