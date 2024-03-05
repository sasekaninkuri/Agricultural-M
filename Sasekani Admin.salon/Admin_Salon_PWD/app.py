
from flask import Flask, request, render_template
from flask_pymongo import PyMongo

login_app = Flask(__name__)

login_app.config["MONGO_URI"] = "mongodb://localhost:5000/AdminSalon"
mongo = PyMongo(login_app)
db = mongo.db

@login_app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Create a user document
        user = {'username': username, 'password': password}

        # Insert the user document into the 'Salon' collection
        db.Salon.insert_one(user)

    return render_template('login.html')

if __name__ == '__main__':
    login_app.run(debug=True)


