from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, store_name):
        store = StoreModel.find_by_store_name(store_name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, store_name):
        if StoreModel.find_by_store_name(store_name):
            return {'message': "A store with store store_name '{}' already exists.".format(store_store_name)}, 400

        store = StoreModel(store_name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, store_name):
        store = StoreModel.find_by_store_name(store_name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
