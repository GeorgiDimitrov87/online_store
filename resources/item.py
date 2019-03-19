from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description',
                        type=str,
                        )
    parser.add_argument('link',
                        type=str,
                        )
    parser.add_argument('image_link',
                        type=str,
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    @jwt_required()
    def get(self, title):
        item = ItemModel.find_by_title(title)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, title):
        if ItemModel.find_by_title(title):
            return {'message': "An item with title '{}' already exists.".format(title)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(title, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, title):
        item = ItemModel.find_by_title(title)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, title):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_title(title)

        if item:
            item.description = data['description']
        else:
            item = ItemModel(title, **data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
