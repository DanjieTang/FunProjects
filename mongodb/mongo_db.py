from pymongo import MongoClient
from typing import Any


class MongoDB:
    def __init__(
        self,
        database_name: str,
        collection_name: str,
        ip_address: str = "localhost",
        port_num: int = 27017,
        uri: str = "",
    ) -> None:
        if uri:
            self.client = MongoClient(uri)
        else:
            self.client = MongoClient(ip_address, port_num)

        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert(self, data: dict[Any, Any] | list[dict[Any, Any]]) -> None:
        """
        Insert some document into database.

        :param data: The document to be inserted.
        """
        if isinstance(data, list):
            self.collection.insert_many(data)
        else:
            self.collection.insert_one(data)

    def query(self, condition: dict[Any, Any] = {}) -> list[dict[Any, Any]]:
        """
        Query the dataset collection, find and return all documents that satisfies
        condition.
        Some examples of condition:
        1. {"age": {"$gt": 21}} -> age is greater than to 21
        2. {"age": 21} -> age is exactly 21
        3. {"name": "Danjie"} -> name is Danjie

        :param condition: Only return documents that satisfies these conditions.
        :return: All documents that satisfies condition.
        """
        result = list(self.collection.find(condition))
        return result

    def view_all_documents(self) -> list[dict[Any, Any]]:
        """
        Return all the dictionary in the collection.

        :return: A list that contains all the documents in the collection,
        each document is an element in the list.
        """
        return list(self.collection.find())

    def delete_documents(self, condition: dict[Any, Any]) -> None:
        """
        Remove all the documents that satisfies the condition.
        Some examples of condition:
        1. {"age": {"$gt": 21}} -> age is greater than to 21
        2. {"age": 21} -> age is exactly 21
        3. {"name": "Danjie"} -> name is Danjie

        :param condition: Condition that tells us what documents are we deleting.
        """
        self.collection.delete_many(condition)

    def clear_collection(self) -> None:
        """
        Remove all the documents in this collection.
        """
        self.collection.delete_many({})

    def update_documents(
        self, condition: dict[Any, Any], modification: dict[str, dict[Any, Any]]
    ) -> None:
        """
        All documents that satisfies condition will be updated.
        Some examples of condition:
        1. {"age": {"$gt": 21}} -> age is greater than to 21
        2. {"age": 21} -> age is exactly 21
        3. {"name": "Danjie"} -> name is Danjie

        Some examples of modifications:
        1. {"$set": {"age": 19}} -> Set age to be 19
        2. {"$inc": {"age": 1}} -> Increase age by one
        3. {"$inc": {"age": -1}} -> Decrease age by one

        :param condition: Only update documents that satisfies these conditions.
        :param modification: The change to be applied.
        """
        self.collection.update_many(condition, modification)

    def count(self, condition: dict[Any, Any] = {}) -> int:
        """
        Find how many number of documents are in the collection.
        Some examples of condition:
        1. {"age": {"$gt": 21}} -> age is greater than to 21
        2. {"age": 21} -> age is exactly 21
        3. {"name": "Danjie"} -> name is Danjie

        :param condition: What condition are we using to count the documents.
        :return: Number of documents in this collection.
        """
        return self.collection.count_documents(condition)
