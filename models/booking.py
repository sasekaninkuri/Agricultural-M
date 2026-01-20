from models.database import mongo

class BookingModel:
    @staticmethod
    def get_bookings_by_date(date):
        db = mongo.db
        return list(db.booking.find({"date": date}))

    @staticmethod
    def get_all_bookings():
        db = mongo.db
        return list(db.booking.find())

    @staticmethod
    def add_booking(categories, date, time, price):
        db = mongo.db
        db.booking.insert_one({
            'categories': categories,
            'date': date,
            'time': time,
            'price': price
        })
