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
    try:
        # 1. Fetch Client Stats
        clients = list(ClientModel.get_all_clients())
        female_count = sum(1 for c in clients if c.get('Gender') == 'Female')
        male_count = sum(1 for c in clients if c.get('Gender') == 'Male')
        other_count = len(clients) - female_count - male_count

        # 2. Fetch Finance Stats
        finances = list(FinanceModel.get_all_finances())
        total_revenue = sum(float(f.get('Amount', 0)) for f in finances)
        
        # 3. Fetch Booking Stats
        bookings = list(BookingModel.get_all_bookings())
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
    except Exception as e:
        print(f"Database Error: {e}")
        # Provide fallback stats so the page still loads even if DB fails
        stats = {
            'clients': {'female': 0, 'male': 0, 'other': 0},
            'finance': {'total': 0},
            'bookings': {'total': 0}
        }
        return render_template("Dashboard.html", stats=stats, db_error=str(e))

@main_bp.route('/settings')
def settings():
    return render_template("settings.html")

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.landing'))
