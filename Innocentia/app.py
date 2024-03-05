
from flask import Flask, render_template, request, url_for, flash 
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/AdminSalon"
Mongo = PyMongo(app)
db = Mongo.db


@app.route('/Resetpassword', methods=["POST","GET"])
def Resetpassword():
  if request.method =="post":
     
     password = request.form["password"]
     confirm_password = request["Confirm password"]

     salondetails = {password:"name"}

     db.AdminSalon.insert_one(salondetails)
     print(password)

  return render_template('signup.html')

if __name__== '_main_':
    app.run(debug=True)
