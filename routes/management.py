from flask import Blueprint, render_template, request, url_for, redirect
from models.finance import FinanceModel
from models.client import ClientModel
from models.booking import BookingModel

mgmt_bp = Blueprint('management', __name__)

@mgmt_bp.route('/Addfinance', methods=["POST", "GET"])
def add_finance():
    if request.method == 'POST':
        date = request.form['Date']
        amount = request.form['price']
        description = request.form['Description']
        FinanceModel.add_finance(date, amount, description)
        return redirect(url_for('management.get_finance'))
    return render_template("Addfinance.html")

@mgmt_bp.route("/finance", methods=["GET"])
def get_finance():
    finance = FinanceModel.get_all_finances()
    return render_template("finance.html", x=finance)

@mgmt_bp.route("/clients", methods=["GET"])
def get_clients():
    all_clients = ClientModel.get_all_clients()
    return render_template("clients.html", x=all_clients)

@mgmt_bp.route("/add_client", methods=["POST", "GET"])
def add_client():
    if request.method == 'POST':
        name = request.form['Name']
        contacts = request.form['Contacts']
        gender = request.form['Gender']
        email = request.form['Email']
        ClientModel.add_client(name, contacts, gender, email)
        return redirect(url_for('management.get_clients'))
    return render_template("AddClient.html")

@mgmt_bp.route('/bookings', methods=["POST", "GET"])
def get_bookings():
    if request.method == 'POST':
        date = request.form['bookingdate']
        booking = BookingModel.get_bookings_by_date(date)
        return render_template("bookings.html", x=booking)
    # Show all bookings by default
    all_bookings = BookingModel.get_all_bookings()
    return render_template("bookings.html", x=all_bookings)

@mgmt_bp.route('/add_booking', methods=["POST", "GET"])
def add_booking():
    if request.method == 'POST':
        categories = request.form['categories']
        date = request.form['date']
        time = request.form['time']
        price = request.form['price']
        BookingModel.add_booking(categories, date, time, price)
        return redirect(url_for('management.get_bookings'))
    return render_template("AddBooking.html")
