from models.database import mongo

class ClientModel:
    @staticmethod
    def get_all_clients():
        db = mongo.db
        return list(db.clients.find())

    @staticmethod
    def add_client(name, contacts, gender, email):
        db = mongo.db
        db.clients.insert_one({
            'Name': name,
            'Contacts': contacts,
            'Gender': gender,
            'Email': email
        })
