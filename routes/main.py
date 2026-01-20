from flask import Blueprint, render_template, session, redirect, url_for
from models.client import ClientModel
from models.finance import FinanceModel
from models.booking import BookingModel

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def landing():
    return render_template("landing.html")

@main_bp.route('/index')
def index():
    # 1. Fetch Client Stats
    clients = ClientModel.get_all_clients()
    female_count = sum(1 for c in clients if c.get('Gender') == 'Female')
    male_count = sum(1 for c in clients if c.get('Gender') == 'Male')
    other_count = len(clients) - female_count - male_count

    # 2. Fetch Finance Stats
    finances = FinanceModel.get_all_finances()
    total_revenue = sum(float(f.get('Amount', 0)) for f in finances)
    
    # 3. Fetch Booking Stats
    bookings = BookingModel.get_all_bookings()
    total_bookings = len(bookings)

    stats = {
        'clients': {
            'female': female_count,
            'male': male_count,
            'other': other_count
        },
        'finance': {
            'total': total_revenue
        },
        'bookings': {
            'total': total_bookings
        }
    }

    return render_template("Dashboard.html", stats=stats)

@main_bp.route('/settings')
def settings():
    return render_template("settings.html")

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.landing'))
