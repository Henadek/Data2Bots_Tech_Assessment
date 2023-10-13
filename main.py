import json
import os


def read_data() -> json:
    # TODO: Reads a JSON file similar to what's present in this location (./data/)
    f_path = os.path.join(os.path.dirname(__file__), 'python_engineer_experienced_professional/data')
    # print(os.listdir(f_path))

    with open(f'{f_path}/data_1.json') as fh:
        json_data = json.load(fh)

    return json_data


def parse_data(json_data) -> json:
    # TODO: Sniffs the schema of the JSON file
    print(json_data.keys())
    pass


def output_data() -> json:
    # TODO: Dumps the output in (./schema/)
    pass



json_data = read_data()
# print(json_data)
processed_data = parse_data(json_data)
print(processed_data)
