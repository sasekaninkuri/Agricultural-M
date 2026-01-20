from models.database import get_db

class ClientModel:
    @staticmethod
    def get_all_clients():
        db = get_db()
        return list(db.clients.find())

    @staticmethod
    def add_client(name, contacts, gender, email):
        db = get_db()
        db.clients.insert_one({
            'Name': name,
            'Contacts': contacts,
            'Gender': gender,
            'Email': email
        })
