import pymongo
from bson import ObjectId


class DB:
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client["evg1"].product

    def get(self, _id: str) -> dict:
        """
        Get product information
        :param _id: hash id (ObjectId as sting)
        :type _id: str
        :return: Product data
        :rtype: dict
        """
        return self.db.find_one({"_id": ObjectId(oid=_id)})

    def put(self, data: dict) -> str:
        """
        Save(insert) JSON data from UI into database
        :param data: JSON to save
        :type data: dict
        :return: ObjectID as string
        :rtype: str
        """
        return str(self.db.insert_one(data).inserted_id)

    def delete(self, _id: str) -> int:
        """
        Remove document from database by given _ID
        :param _id: hash id (ObjectId as sting)
        :type _id: str
        :return: Count of deleted documents
        :rtype: int
        """
        return self.db.delete_one({"_id": ObjectId(oid=_id)}).deleted_count
