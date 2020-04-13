import datetime
from typing import Optional


class Validate:
    def __init__(self, json: dict):
        self.data = json
        self._required = self.__get_required()

    def insert(self) -> Optional[dict]:
        """
        Check and reformat JSON on insert
        Date will be changed from string to datetime object
        If one of required fields are absent - return None
        :return: Reformatted JSON or None
        :rtype: Optional[dict]
        """
        if not self.__is_required_at_place():
            return None
        if not self.__is_required_not_empty():
            return None
        self.__quantity_reformat()
        self.__date_reformat()
        return self.data

    def __is_required_at_place(self) -> bool:
        """
        Check if JSON keys have all of required fields
        :return: True or False
        :rtype: bool
        """
        for key in self._required:
            if key not in self.data.keys():
                return False
        return True

    def __is_required_not_empty(self) -> bool:
        """
        Check if required fields anr not empty (have no value)
        :return: True or False
        :rtype: bool
        """
        for key in self._required:
            if not self.data[key]:
                return False
        return True

    def __quantity_reformat(self):
        """
        Reformat quantity from str to float
        :return: None
        :rtype: None
        """
        self.data["quantity"] = float(self.data["quantity"])

    def __date_reformat(self):
        """
        Reformat date in JSON if needed
        :return: None
        :rtype: None
        """
        raw_date = self.data["expiration"]
        date_list = raw_date.split("-")  # len(date_list) must be equal to 3
        date = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        self.data["expiration"] = date

    @staticmethod
    def __get_required():
        return [
            "name",
            "quantity",
            "units",
            "expiration",
        ]
