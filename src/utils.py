import json
from datetime import datetime
import re


def load_file():
    '''загрузка JSON файла'''

    with open('../operations.json', 'r', encoding='Utf-8') as file:
        return json.load(file)


def sort_data(data):
    '''вывод выполненных операций, сортировка по дате'''

    # List compression который исключает {}, и не выполненные операции
    data = [
        operate_dict
        for operate_dict in data
        if operate_dict != {} and operate_dict['state'] == 'EXECUTED'
    ]

    # Сортировка по дате
    data = sorted(
        data,
        key=lambda operation_date: operation_date['date'],
        reverse=True
    )

    # Возврат последних пяти операций
    return data[:5]


def redact_operate_date(date):
    '''Формат даты'''

    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date = datetime.strftime(date, '%d.%m.%Y')

    return date


def hide_sender_account(numbers: str):
    '''Формат номера счета отправителя'''

    return f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"


def hide_recipient_account(numbers: str):
    '''Формат номера счета получателя'''

    return f"**{numbers[-4:]}"


def operations_short_check(data):
    '''Выовод последних пяти операций в удобном формате'''

    short_info = []
    for operation in data:

        # Условие присутствия отправителя
        if 'from' in operation:

            # окончательное форматирование данных об операции
            name_from = ''.join(re.findall('[a-zA-Zа-яА-Я]+', operation['from']))
            numbers_from = ''.join(re.findall('\d+', operation['from']))
            name_to = ''.join(re.findall('[a-zA-Zа-яА-Я]+', operation['to']))
            numbers_to = ''.join(re.findall('\d+', operation['to']))

            short_info.append(f"{redact_operate_date(operation['date'])} {operation['description']}\n"
                              f"{name_from} {hide_sender_account(numbers_from)} -> {name_to} {hide_recipient_account(numbers_to)}\n"
                              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        else:

            name_to = ''.join(re.findall('[a-zA-Zа-яА-Я]+', operation['to']))
            numbers_to = ''.join(re.findall('\d+', operation['to']))

            short_info.append(f"{redact_operate_date(operation['date'])} {operation['description']}\n"
                              f"{name_to} {hide_recipient_account(numbers_to)}\n"
                              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")

    return '\n\n'.join(short_info)