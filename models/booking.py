from models.database import get_db

class BookingModel:
    @staticmethod
    def get_bookings_by_date(date):
        db = get_db()
        return list(db.booking.find({"date": date}))

    @staticmethod
    def get_all_bookings():
        db = get_db()
        return list(db.booking.find())

    @staticmethod
    def add_booking(categories, date, time, price):
        db = get_db()
        db.booking.insert_one({
            'categories': categories,
            'date': date,
            'time': time,
            'price': price
        })
