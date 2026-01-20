from models.database import mongo

class ServiceModel:
    @staticmethod
    def add_hairstyle(name, price):
        db = mongo.db
        return db.Hairstyle.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_hairstyles():
        db = mongo.db
        return list(db.Hairstyle.find())

    @staticmethod
    def add_haircut(name, price):
        db = mongo.db
        return db.haircut.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_haircuts():
        db = mongo.db
        return list(db.haircut.find())

    @staticmethod
    def add_nails(name, price):
        db = mongo.db
        return db.Nails.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_nails():
        db = mongo.db
        return list(db.Nails.find())

    @staticmethod
    def add_makeup(name, price):
        db = mongo.db
        return db.Makeup.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_makeup():
        db = mongo.db
        return list(db.Makeup.find())

    @staticmethod
    def add_weave(name, price):
        db = mongo.db
        return db.Weaves.insert_one({'name': name, 'price': price})

    @staticmethod
    def get_all_weaves():
        db = mongo.db
        return list(db.Weaves.find())
