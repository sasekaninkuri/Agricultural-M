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
