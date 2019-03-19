from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(400))
    link = db.Column(db.String(100))
    image_link = db.Column(db.String(200))



    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, title , description, link, image_link, store_id):
        self.title  = title 
        self.description = description
        self.link = link
        self.image_link = image_link
        self.store_id = store_id

    def json(self):
        return {'title ': self.title , 'description': self.description , 'link': self.link , 'image_link': self.image_link}

    @classmethod
    def find_by_title (cls, title ):
        return cls.query.filter_by(title =title ).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
