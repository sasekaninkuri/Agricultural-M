from flask import Blueprint, render_template, request, url_for, redirect
from models.finance import FinanceModel
from models.client import ClientModel
from models.booking import BookingModel
from models.staff import StaffModel
from models.inventory import InventoryModel
from models.promotion import PromotionModel
from models.gallery import GalleryModel
from models.review import ReviewModel

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

# --- STAFF ROUTES ---
@mgmt_bp.route("/staff", methods=["GET"])
def get_staff():
    all_staff = StaffModel.get_all_staff()
    return render_template("staff.html", staff=all_staff)

@mgmt_bp.route("/add_staff", methods=["POST", "GET"])
def add_staff():
    if request.method == 'POST':
        name = request.form['Name']
        role = request.form['Role']
        specialty = request.form['Specialty']
        contacts = request.form['Contacts']
        email = request.form['Email']
        StaffModel.add_staff(name, role, specialty, contacts, email)
        return redirect(url_for('management.get_staff'))
    return render_template("AddStaff.html")

# --- INVENTORY ROUTES ---
@mgmt_bp.route("/inventory", methods=["GET"])
def get_inventory():
    inventory = InventoryModel.get_all_inventory()
    return render_template("inventory.html", inventory=inventory)

@mgmt_bp.route("/add_inventory", methods=["POST", "GET"])
def add_inventory():
    if request.method == 'POST':
        name = request.form['Name']
        category = request.form['Category']
        count = request.form['Count']
        price = request.form['Price']
        description = request.form['Description']
        InventoryModel.add_item(name, category, count, price, description)
        return redirect(url_for('management.get_inventory'))
    return render_template("AddInventory.html")

# --- PROMOTION ROUTES ---
@mgmt_bp.route("/promotions", methods=["GET"])
def get_promotions():
    promotions = PromotionModel.get_all_promotions()
    return render_template("promotions.html", promotions=promotions)

@mgmt_bp.route("/add_promotion", methods=["POST", "GET"])
def add_promotion():
    if request.method == 'POST':
        name = request.form['Name']
        discount = request.form['Discount']
        start_date = request.form['StartDate']
        end_date = request.form['EndDate']
        description = request.form['Description']
        PromotionModel.add_promotion(name, discount, start_date, end_date, description)
        return redirect(url_for('management.get_promotions'))
    return render_template("AddPromotion.html")

# --- GALLERY ROUTES ---
@mgmt_bp.route("/gallery", methods=["GET"])
def get_gallery():
    images = GalleryModel.get_all_images()
    return render_template("gallery.html", images=images)

@mgmt_bp.route("/add_image", methods=["POST", "GET"])
def add_image():
    if request.method == 'POST':
        title = request.form['Title']
        category = request.form['Category']
        image_url = request.form['ImageUrl']
        description = request.form['Description']
        GalleryModel.add_image(title, category, image_url, description)
        return redirect(url_for('management.get_gallery'))
    return render_template("AddImage.html")

# --- REVIEW ROUTES ---
@mgmt_bp.route("/reviews", methods=["GET"])
def get_reviews():
    reviews = ReviewModel.get_all_reviews()
    # Calculate average rating
    avg_rating = 0
    if len(reviews) > 0:
        total = sum([float(r.get('Rating', 0)) for r in reviews])
        avg_rating = round(total / len(reviews), 1)
        
    return render_template("reviews.html", reviews=reviews, avg_rating=avg_rating)

@mgmt_bp.route("/add_review", methods=["POST", "GET"])
def add_review():
    if request.method == 'POST':
        client_name = request.form['ClientName']
        rating = request.form['Rating']
        comment = request.form['Comment']
        date = request.form['Date']
        ReviewModel.add_review(client_name, rating, comment, date)
        return redirect(url_for('management.get_reviews'))
    return render_template("AddReview.html")
