import unittest
import json
import os

f_path = os.path.join(os.path.dirname(__file__))
with open(f'{f_path}/schema/schema_1.json') as fh:
    output_data = json.load(fh)


class MyTestCase(unittest.TestCase):
    def test_tag_padding(self):
        for key in output_data:
            if key != 'participantIds':
                self.assertIn('tag', output_data[key])

    def test_description_padding(self):
        for key in output_data:
            if key != 'participantIds':
                self.assertIn('description', output_data[key])

    def test_required_padding(self):
        for key in output_data:
            if key != 'participantIds':
                self.assertIn('required', output_data[key])

    def test_required_value(self):
        for key in output_data:
            if key != 'participantIds':
                self.assertEqual(output_data[key]['required'], False)

