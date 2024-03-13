from flask import Flask, render_template, request, url_for, redirect,Response
from flask_pymongo import PyMongo
from bson.objectid import *
import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/SalonAdmin"
Mongo = PyMongo(app)
db = Mongo.db

# landing page
@app.route('/')
def landing():
        return render_template("landing.html")

# Signup page

@app.route('/signup', methods=["POST","GET"])
def signup():
  if request.method =="POST":
     name = request.form["name"]
     email = request.form["email"]
     address = request.form["Address"]
     password = request.form["password"]
     Confirm_Pasword = request.form["confirm password"]
     
    #  confirming password
   
     if password != Confirm_Pasword:
      return "passwords do not match"


     admindetails = {"name":name, "email":email, "address":address, "password":password}

     db.admin.insert_one(admindetails)

     if ('form submission success'):
                     return redirect (url_for('login'))
     else:

                  if ('form submission failed'):
                   return 'form unsuccessful'

  return render_template('signup.html')


# Login page
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        
        admindetails = {'name': name, 'password':password}
        

    try:
     
        user = db.admin.find_one(admindetails)

        if user is None:
         return redirect(url_for('signup'))
        else:
         return redirect(url_for('index'))
    except Exception as e:
     print("An error occurred:", e)


    return render_template('login.html')

@app.route("/resetpas", methods=['PATCH'] )
def resetpas():

      result=db.admin.update_one({"_id":ObjectId()},{"$set":{'name': request.form['name']}})

    
      
      if result.modified_count == 1:
          return Response(
                           response= json.dumps({"message":"Did not update"}),
                           status=200,
                           mimetype="application/json"

                      )
      return render_template('resetpas.html')

@app.route("/hairstle", methods=["POST", "GET"] )
def getHair():
     if request.method == 'Get':
          for i in db.Hairstyle.find():
               print(i)
     
     return render_template("hairstyle.html")


@app.route('/index')
def index():
       return "login"
    
if __name__ == "__main__":
    app.run (debug=True)