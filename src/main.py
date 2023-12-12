import utils

all_operations_data = utils.load_file()
sort_data = utils.sort_data(all_operations_data)

print(utils.operations_short_check(sort_data))