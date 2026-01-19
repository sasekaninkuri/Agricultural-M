from models.database import mongo

class FinanceModel:
    @staticmethod
    def add_finance(date, amount, description):
        db = mongo.db
        return db.finances.insert_one({'Date': date, 'Amount': amount, 'Description': description})

    @staticmethod
    def get_all_finances():
        db = mongo.db
        return list(db.finances.find())
