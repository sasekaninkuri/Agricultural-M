from flask import Blueprint, render_template, request, url_for, redirect, Response, session, flash
from models.admin import AdminModel
from bson.objectid import ObjectId
import json

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        address = request.form["Address"]
        password = request.form["password"]
        confirm_password = request.form["confirm password"]
        
        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template('signup.html')

        AdminModel.create_admin(name, email, address, password)
        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('signup.html')

@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        identifier = request.form['username'].strip()
        password = request.form['password']
        
        print(f"Login attempt for: {identifier}")

        try:
            user = AdminModel.find_admin(identifier, password)
            if user is None:
                print(f"User not found or password incorrect for: {identifier}")
                flash("Invalid Salon Name/Email or Password", "danger")
                return redirect(url_for('auth.login')) # Redirect to login, not signup
            else:
                print(f"Login successful for: {user['name']}")
                session['user'] = user['name']  # Store the actual name from DB
                return redirect(url_for('main.index'))
        except Exception as e:
            print("An error occurred during login:", e)
            flash("An error occurred. Please try again.", "danger")

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('main.landing'))

@auth_bp.route("/resetpas", methods=['GET', 'PATCH'])
def resetpas():
    if request.method == 'PATCH':
        # Note: The original logic used ObjectId() without a specific ID, which always creates a new ID.
        # This seems like a placeholder in the original code. I'll preserve the behavior but use the model.
        result = AdminModel.update_admin_name(ObjectId(), request.form['name'])
        if result.modified_count == 1:
            return Response(
                response=json.dumps({"message": "Updated successfully"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps({"message": "Did not update"}),
            status=200,
            mimetype="application/json"
        )
    return render_template('resetpas.html')
