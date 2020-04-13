import datetime

from logic.validate import Validate


class TestValidate:
    def test_validate_insertation1(self):
        json = {
            "name": "Potato",
            "quantity": 14,
            "units": "unit",
            "expiration": "2020-05-13",
            "note": "In green bag"
        }
        checked = Validate(json).insert()
        assert isinstance(checked, dict) and checked["expiration"] == datetime.datetime(2020, 5, 13, 0, 0)

    def test_validate_insertation_required_less1(self):
        json = {
            "name": "Potato",
            "units": "unit",
            "expiration": "2020-05-13",
            "note": "In green bag"
        }
        checked = Validate(json).insert()
        assert isinstance(checked, type(None))

    def test_validate_insertation_required_empty1(self):
        json = {
            "name": "Potato",
            "units": "unit",
            "quantity": 0,
            "expiration": "",
            "note": "In green bag"
        }
        checked = Validate(json).insert()
        assert isinstance(checked, type(None))
