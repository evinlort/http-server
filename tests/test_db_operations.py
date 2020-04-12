import datetime

import pytest

from logic.db import DB

pytest.ins_id = ""


class TestDB:
    def test_insert1(self):
        data = {
            "name": "Potato",
            "quantity": 14,
            "units": "unit",
            "expiration": datetime.datetime(2020, 5, 13),
            "note": "In green bag"
        }
        resp = DB().put(data)
        assert isinstance(resp, str) and len(resp) == 24
        pytest.ins_id = resp

    def test_get1(self):
        assert DB().get(pytest.ins_id)["units"] == "unit"

    def test_delete1(self):
        data = pytest.ins_id
        ret = DB().delete(data)
        assert ret == 1
