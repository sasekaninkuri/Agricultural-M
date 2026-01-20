from models.database import get_db

class ServiceModel:
    @staticmethod
    def add_hairstyle(name, price):
        db = get_db()
        return db.Hairstyle.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_hairstyles():
        db = get_db()
        return list(db.Hairstyle.find())

    @staticmethod
    def add_haircut(name, price):
        db = get_db()
        return db.haircut.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_haircuts():
        db = get_db()
        return list(db.haircut.find())

    @staticmethod
    def add_nails(name, price):
        db = get_db()
        return db.Nails.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_nails():
        db = get_db()
        return list(db.Nails.find())

    @staticmethod
    def add_makeup(name, price):
        db = get_db()
        return db.Makeup.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_makeup():
        db = get_db()
        return list(db.Makeup.find())

    @staticmethod
    def add_weave(name, price):
        db = get_db()
        return db.Weaves.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_weaves():
        db = get_db()
        return list(db.Weaves.find())
