from logic.db import DB
from logic.validate import Validate


class TestValidateAndSave:
    def test_validate_and_save1(self):
        json = {
            "name": "Potato",
            "units": "unit",
            "quantity": 0,
            "expiration": "",
            "note": "In green bag"
        }
        checked = Validate(json).insert()
        answer = DB("product").put(checked)
        assert isinstance(answer, str) and answer == "Validation did not passed."
