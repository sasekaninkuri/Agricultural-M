from models.database import get_db

class StaffModel:
    @staticmethod
    def get_all_staff():
        db = get_db()
        return list(db.staff.find())

    @staticmethod
    def add_staff(name, role, specialty, contacts, email):
        db = get_db()
        db.staff.insert_one({
            'Name': name,
            'Role': role,
            'Specialty': specialty,
            'Contacts': contacts,
            'Email': email
        })

    @staticmethod
    def delete_staff(staff_id):
        # Implementation for later
        pass
