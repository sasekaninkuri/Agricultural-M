from models.database import mongo

class AdminModel:
    @staticmethod
    def create_admin(name, email, address, password):
        db = mongo.db
        admindetails = {"name": name, "email": email, "address": address, "password": password}
        return db.admin.insert_one(admindetails)

    @staticmethod
    def find_admin(identifier, password):
        db = mongo.db
        # Use regex for case-insensitive matching on name or email
        return db.admin.find_one({
            "$or": [
                {"name": {"$regex": f"^{identifier}$", "$options": "i"}},
                {"email": {"$regex": f"^{identifier}$", "$options": "i"}}
            ],
            "password": password
        })

    @staticmethod
    def update_admin_name(admin_id, new_name):
        db = mongo.db
        return db.admin.update_one({"_id": admin_id}, {"$set": {'name': new_name}})
