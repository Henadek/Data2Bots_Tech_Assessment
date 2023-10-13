import json
import os


def read_data() -> dict:
    # TODO: Reads a JSON file similar to what's present in this location (./data/)
    f_path = os.path.join(os.path.dirname(__file__), 'python_engineer_experienced_professional/data')
    # print(os.listdir(f_path))

    with open(f'{f_path}/data_1.json') as fh:
        json_data = json.load(fh)

    return json_data


def parse_data(json_data: dict) -> dict:
    # TODO: Sniffs the schema of the JSON file
    parsed_data = None
    for i in json_data.keys():
        if i == 'message':
            message_keys = json_data[i].keys()
            for attr in message_keys:
                # print(attr)
                json_data[i][attr]
                # add tag and description keys
                try:
                    json_data[i][attr]['tag'] = ''
                    json_data[i][attr]['description'] = ''
                    json_data[i][attr]['required'] = False
                except TypeError:
                    pass
    parsed_data = json_data

    return parsed_data['message']


def output_data(parsed_data: dict) -> json:
    # TODO: Dumps the output in (./schema/)
    f_path = os.path.join(os.path.dirname(__file__), 'python_engineer_experienced_professional/schema')

    with open(f'{f_path}/schema_1.json', 'w') as fh:
        json.dump(parsed_data, fh)

    return parsed_data


json_data = read_data()
processed_data = parse_data(json_data)
result = output_data(processed_data)
print(result)
