import json
import os


def read_data(json_file: json) -> dict:
    # TODO: Reads a JSON file similar to what's present in this location (./data/)
    with open(json_file) as fh:
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


def output_data(parsed_data: dict, json_file: json) -> json:
    # TODO: Dumps the output in (./schema/)
    with open(json_file, 'w') as fh:
        json.dump(parsed_data, fh)

    return parsed_data


f_path = os.path.join(os.path.dirname(__file__), 'python_engineer_experienced_professional/data')
for i in os.listdir(f_path):
    cwd_path = f'{f_path}/{i}'
    json_data = read_data(cwd_path)
    processed_data = parse_data(json_data)
    output_file = cwd_path.replace('data', 'schema')
    result = output_data(processed_data, output_file)
    print(result)

