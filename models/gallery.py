from models.database import mongo

class GalleryModel:
    @staticmethod
    def get_all_images():
        db = mongo.db
        return list(db.gallery.find())

    @staticmethod
    def add_image(title, category, image_url, description):
        db = mongo.db
        db.gallery.insert_one({
            'Title': title,
            'Category': category,
            'ImageUrl': image_url,
            'Description': description
        })
