from flask import Blueprint, render_template, request, url_for, redirect
from models.service import ServiceModel

services_bp = Blueprint('services', __name__)

@services_bp.route('/add_hairstyle', methods=["POST", "GET"])
def add_hairstyle():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        ServiceModel.add_hairstyle(name, price)
        return redirect(url_for('services.get_hair'))
    return render_template("AddHairstyle.html")

@services_bp.route("/hairstyle", methods=["GET"])
def get_hair():
    hair = ServiceModel.get_all_hairstyles()
    return render_template("hairstyle.html", x=hair)

@services_bp.route('/Addhaircut', methods=["POST", "GET"])
def add_haircut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        ServiceModel.add_haircut(name, price)
        return redirect(url_for('services.get_cut'))
    return render_template("Addhaircut.html")

@services_bp.route("/haircut", methods=["GET"])
def get_cut():
    cut = ServiceModel.get_all_haircuts()
    return render_template("haircut.html", x=cut)

@services_bp.route('/AddNails', methods=["POST", "GET"])
def add_nails():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        ServiceModel.add_nails(name, price)
        return redirect(url_for('services.get_nails'))
    return render_template("AddNails.html")

@services_bp.route("/nails", methods=["GET"])
def get_nails():
    nails = ServiceModel.get_all_nails()
    return render_template("nails.html", x=nails)

@services_bp.route('/AddMakeup', methods=["POST", "GET"])
def add_makeup():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        ServiceModel.add_makeup(name, price)
        return redirect(url_for('services.get_makeup'))
    return render_template("AddMakeup.html")

@services_bp.route("/Makeup", methods=["GET"])
def get_makeup():
    up = ServiceModel.get_all_makeup()
    return render_template("Makeup.html", x=up)

@services_bp.route('/AddWeave', methods=["POST", "GET"])
def add_weave():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        ServiceModel.add_weave(name, price)
        return redirect(url_for('services.get_weaves'))
    return render_template("AddWeave.html")

@services_bp.route("/Weave_installation", methods=["GET"])
def get_weaves():
    weave = ServiceModel.get_all_weaves()
    return render_template("Weave_installation.html", x=weave)
