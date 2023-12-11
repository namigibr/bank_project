import json


def load_file():
    with open('operations.json', 'r', encoding='Utf-8') as file:
        return json.load(file)


def sort_data(data):
    data = [
        operate_dict
        for operate_dict in data
        if operate_dict != {} and operate_dict['state'] == 'EXECUTED'
        ]

    data = sorted(
        data,
        key=lambda operation_date: operation_date['date'],
        reverse=True
    )

    return data




