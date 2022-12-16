import unittest
from task2.task2_manual import Manual
from task2.task2_lib import Lib

class MyTestCase(unittest.TestCase):
    def test_convert_to_json_empty(self):
        converter = Manual([''])
        lib_conv = Lib([''])
        self.assertEqual(converter.convert_data_to_json(), '[]')
        self.assertEqual(lib_conv.convert_data_to_json(), '[]')
    def test_convert_to_json_normal(self):
        test_text1 = ['id,name,birth,salary,department\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n', '3,Ivan,,130000,8']
        converter = Manual(test_text1)
        self.assertEqual(converter.convert_data_to_json(), '''[{ "id":    "1" ,"name":    "Ivan" ,"birth":    "1980" ,"salary":    "150000" ,"department":    "1"  },{ "id":    "2" ,"name":    "Alex" ,"birth":    "1960" ,"salary":    "200000" ,"department":    "5"  },{ "id":    "3" ,"name":    "Ivan" ,"birth":    "" ,"salary":    "130000" ,"department":    "8"  }]''')
    def test_convert_to_json_title(self):
        test_text2 = ['id,name,birth,salary,department']
        lib_conv = Lib(test_text2)
        converter = Manual(test_text2)
        self.assertEqual(converter.convert_data_to_json(), '[]')
        self.assertEqual(lib_conv.convert_data_to_json(), '[]')


if __name__ == '__main__':
    unittest.main()
