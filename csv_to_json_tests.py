import unittest
from csv_to_json import Manual
from csv_to_json_lib import Lib

class MyTestCase(unittest.TestCase):
    def test_convert_to_json(self):
        converter = Manual()
        lib_conv = Lib()
        self.assertEqual(converter.convert_data_to_json(''), '')
        test_text1 = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n', '3,Ivan,,130000,8']
        self.assertEqual(converter.convert_data_to_json(test_text1), '''[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150000",
        "department": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200000",
        "department": "5"
    },
    {
        "id": "3",
        "name": "Ivan",
        "birth": "",
        "salary": "130000",
        "department": "8"
    }
]''')
        test_text2 = ['id,name,birth,salary,department']
        self.assertEqual(converter.convert_data_to_json(test_text2), '[]')
        self.assertEqual(converter.convert_data_to_json(test_text1), lib_conv.convert_data_to_json(test_text1))


if __name__ == '__main__':
    unittest.main()
