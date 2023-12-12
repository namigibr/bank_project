from src import utils


def test_sort_data(data_test_file):
    assert utils.sort_data(data_test_file) == [{'id': 142264268,
                                                'state': 'EXECUTED',
                                                'date': '2019-04-04T23:20:05.206878'},
                                               {'id': 214024827,
                                                'state': 'EXECUTED',
                                                'date': '2018-12-20T16:43:26.929246'},
                                               {'id': 939719570,
                                                'state': 'EXECUTED',
                                                'date': '2018-06-30T02:08:58.425572'}]


def test_redact_operate_date(date_test_list):
    assert utils.redact_operate_date(date_test_list[0]) == "12.09.2018"
    assert utils.redact_operate_date(date_test_list[1]) == "29.11.2018"
    assert utils.redact_operate_date(date_test_list[2]) == "11.09.2019"


def test_hide_sender_nums(numbers):
    assert utils.hide_sender_account(numbers) == "9758 48** **** 8967"


def test_hide_recipient_nums(numbers):
    assert utils.hide_recipient_account(numbers) == "**8967"
