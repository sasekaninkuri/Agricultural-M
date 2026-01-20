from models.database import get_db

class FinanceModel:
    @staticmethod
    def add_finance(date, amount, description):
        db = get_db()
        return db.finances.insert_one({'Date': date, 'Amount': amount, 'Description': description})

    @staticmethod
    def get_all_finances():
        db = get_db()
        return list(db.finances.find())
