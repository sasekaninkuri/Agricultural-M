from models.database import get_db

class InventoryModel:
    @staticmethod
    def get_all_inventory():
        db = get_db()
        return list(db.inventory.find())

    @staticmethod
    def add_item(name, category, count, price, description):
        db = get_db()
        db.inventory.insert_one({
            'Name': name,
            'Category': category,
            'Count': count,
            'Price': price,
            'Description': description
        })
