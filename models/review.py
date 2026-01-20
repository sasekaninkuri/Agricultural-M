from models.database import get_db

class ReviewModel:
    @staticmethod
    def get_all_reviews():
        db = get_db()
        return list(db.reviews.find())

    @staticmethod
    def add_review(client_name, rating, comment, date):
        db = get_db()
        db.reviews.insert_one({
            'ClientName': client_name,
            'Rating': rating,
            'Comment': comment,
            'Date': date
        })
