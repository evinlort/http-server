from typing import List

import pymongo
from bson import ObjectId


class DB:
    def __init__(self, table):
        client = pymongo.MongoClient()
        self.db = client["evg1"][table]

    def get(self, _id: str) -> dict:
        """
        Get one collection record information by ObjectId represented by string
        :param _id: hash id (ObjectId as sting)
        :type _id: str
        :return: Record data
        :rtype: dict
        """
        return self.db.find_one({"_id": ObjectId(oid=_id)})

    def getby(self, query: dict) -> dict:
        """
        Get one collection record information by query represented by dictionary
        :param query: Query dictionary
        :type query: dict
        :return: Record date
        :rtype: dict
        """
        return self.db.find_one(query)

    def put(self, data: dict) -> str:
        """
        Save(insert) JSON data from UI into database
        :param data: JSON to save
        :type data: dict
        :return: ObjectID as string
        :rtype: str
        """
        if not data:
            return "Validation did not passed."
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

    def all(self) -> List[dict]:
        """
        Get all records from collection as list of dictionaries
        :return: List of dicts - all records from collection
        :rtype: List[dict]
        """
        return list(self.db.find({}))
