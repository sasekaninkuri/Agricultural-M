from models.database import get_db

class PromotionModel:
    @staticmethod
    def get_all_promotions():
        db = get_db()
        return list(db.promotions.find())

    @staticmethod
    def add_promotion(name, discount, start_date, end_date, description):
        db = get_db()
        db.promotions.insert_one({
            'Name': name,
            'Discount': discount,
            'StartDate': start_date,
            'EndDate': end_date,
            'Description': description
        })
