from models.database import mongo

class ClientModel:
    @staticmethod
    def get_all_clients():
        db = mongo.db
        return list(db.clients.find())
