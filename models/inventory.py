from models.database import mongo

class InventoryModel:
    @staticmethod
    def get_all_inventory():
        db = mongo.db
        return list(db.inventory.find())

    @staticmethod
    def add_item(name, category, count, price, description):
        db = mongo.db
        db.inventory.insert_one({
            'Name': name,
            'Category': category,
            'Count': count,
            'Price': price,
            'Description': description
        })
