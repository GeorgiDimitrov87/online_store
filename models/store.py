from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, shop_name):
        self.shop_name = shop_name

    def json(self):
        return {'shop_name': self.shop_name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_shop_name(cls, shop_name):
        return cls.query.filter_by(shop_name=shop_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
