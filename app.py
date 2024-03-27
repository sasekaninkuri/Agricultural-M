from flask import Flask, render_template, request, url_for, redirect,Response, url_for
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

#Reset Password
# Not yet functioning
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

# Add Hairstyle

@app.route('/add_hairstyle', methods=["POST", "GET"])
def add_service():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        hairtyle = { 'name': name, 'price': price}

        db.Hairstyle.insert_one(hairtyle)
        if ('form submission success'):
                     return redirect (url_for('getHair'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddHairstyle.html")
    

    
# display hairstyle

@app.route("/hairstyle", methods=["POST", "GET"] )
def getHair():
     if request.method == 'GET':
          hair = []

          for i in db.Hairstyle.find():
            hair.append(i)
            
             
     
     return render_template("hairstyle.html" , x=hair )


# add haircut
@app.route('/Addhaircut', methods=["POST", "GET"])
def Addhaircut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        haircut = { 'name': name, 'price': price}

        db.haircut.insert_one(haircut)
        if ('form submission success'):
                     return redirect (url_for('getCut'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("Addhaircut.html")

#Display haircut
@app.route("/haircut", methods=["POST", "GET"] )
def getCut():
     if request.method == 'GET':
          cut = []

          for i in db.haircut.find():
            cut.append(i)
            
             
     
     return render_template("haircut.html" , x=cut )

#Add Nails
@app.route('/AddNails', methods=["POST", "GET"])
def add_nails():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        nails = { 'name': name, 'price': price}

        db.Nails.insert_one(nails)
        if ('form submission success'):
                     return redirect (url_for('getNails'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddNails.html")

#Display Nails
@app.route("/nails", methods=["POST", "GET"] )
def getNails():
     if request.method == 'GET':
          nails = []

          for i in db.Nails.find():
            nails.append(i)
            
             
     
     return render_template("nails.html" , x=nails )

#Add Makeup
@app.route('/AddMakeup', methods=["POST", "GET"])
def add_makeup():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        Makeup = { 'name': name, 'price': price}

        db.Makeup.insert_one(Makeup)
        if ('form submission success'):
                     return redirect (url_for('getMakeup'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddMakeup.html")

#Display Makeup
@app.route("/Makeup", methods=["POST", "GET"] )
def getMakeup():
     if request.method == 'GET':
          up = []

          for i in db.Makeup.find():
            up.append(i)
            
             
     
     return render_template("Makeup.html" , x=up )

#Add Weave
@app.route('/AddWeave', methods=["POST", "GET"])
def add_weave():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        Weaves = { 'name': name, 'price': price}

        db.Weaves.insert_one(Weaves)
        if ('form submission success'):
                     return redirect (url_for('getWeaves'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddWeave.html")

#Display Weave
@app.route("/Weave_installation", methods=["POST", "GET"] )
def getWeaves():
     if request.method == 'GET':
          weave = []

          for i in db.Weaves.find():
            weave.append(i)
            
             
     
     return render_template("Weave_installation.html" , x=weave )
 
 #Add finance
@app.route('/Addfinance', methods=["POST", "GET"])
def add_finance():
    if request.method == 'POST':
        Date = request.form['Date']
        Amount = request.form['price']
        Description = request.form['Description']
        
        finances = { 'Date': Date, 'Amount': Amount,'Description': Description,}

        db.finances.insert_one(finances)
        if ('form submission success'):
                     return redirect (url_for('getFinance'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("Addfinance.html")

#Display Finance
@app.route("/finance", methods=["POST", "GET"] )
def getFinance():
     if request.method == 'GET':
          finance = []

          for i in db.finances.find():
            finance.append(i)
            
             
     
     return render_template("finance.html" , x=finance )
 



# Clients page
@app.route("/clients", methods=["POST", "GET"] )
def getClients():
     if request.method == 'GET':
          all_clients = []
          for x in db.clients.find():
                all_clients.append(x)
            
             
     
     return render_template("clients.html" , x=all_clients )

# @app.route('/Addfinance', methods=["POST", "GET"])
# def add_finance():
#     if request.method == 'POST':
#         Date = request.form['Date']
#         Amount = request.form['Amount']
#         Description = request.form['Description']
        
        
#         finances = { 'Date': Date, 'Amount': Amount,'Description': Description,}

#         db.finances.insert_one(finances)
#         if ('form submission success'):
#                     return redirect (url_for("getFinance"))
#         else:

#                   if ('form submission failed'):
#                    return 'form unsuccessful'
#     return render_template()

@app.route('/index')
def index():
       
       return render_template("Dashboard.html")
    
if __name__ == "__main__":
    app.run (debug=True)