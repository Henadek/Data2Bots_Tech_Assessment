import unittest
import json
import os

f_path = os.path.join(os.path.dirname(__file__), 'schema')
f_path_list = [f'{f_path}/{i}' for i in os.listdir(f_path) if 'schema' in i]
output_data = []
for i in f_path_list:
    with open(i) as fh:
        output_data.append(json.load(fh))


class MyTestCase(unittest.TestCase):
    def test_tag_padding(self):
        for each in output_data:
            for key in each:
                if type(each[key]) is dict:
                    self.assertIn('tag', each[key])

    def test_description_padding(self):
        for each in output_data:
            for key in each:
                if type(each[key]) is dict:
                    self.assertIn('description', each[key])

    def test_required_padding(self):
        for each in output_data:
            for key in each:
                if type(each[key]) is dict:
                    self.assertIn('required', each[key])

    def test_required_value(self):
        for each in output_data:
            for key in each:
                if type(each[key]) is dict:
                    self.assertEqual(each[key]['required'], False)

