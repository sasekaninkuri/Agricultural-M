from models.database import mongo

class ReviewModel:
    @staticmethod
    def get_all_reviews():
        db = mongo.db
        return list(db.reviews.find())

    @staticmethod
    def add_review(client_name, rating, comment, date):
        db = mongo.db
        db.reviews.insert_one({
            'ClientName': client_name,
            'Rating': rating,
            'Comment': comment,
            'Date': date
        })
