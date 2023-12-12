import pytest


@pytest.fixture()
def data_test_file():
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572"
        }, {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        }, {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        }, {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        },
        {}]


@pytest.fixture()
def date_test_list():
    return ["2018-09-12T21:27:25.241689",
            "2018-11-29T07:18:23.941293",
            "2019-09-11T17:30:34.445824"]


@pytest.fixture()
def numbers():
    return "97584898735659638967"