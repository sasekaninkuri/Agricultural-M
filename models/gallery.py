from models.database import get_db

class GalleryModel:
    @staticmethod
    def get_all_images():
        db = get_db()
        return list(db.gallery.find())

    @staticmethod
    def add_image(title, category, image_url, description):
        db = get_db()
        db.gallery.insert_one({
            'Title': title,
            'Category': category,
            'ImageUrl': image_url,
            'Description': description
        })
