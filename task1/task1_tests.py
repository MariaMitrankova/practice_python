import unittest
from task1 import get_titles, prepare_data, add_new_data

class MyTestCase(unittest.TestCase):
    def test_get_titles(self):
        data = '# title Hello world\n# description Some description for out task'
        title, description = get_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')

    def test_get_empty_titles(self):
        data = ''
        title, description = get_titles(data)
        self.assertEqual(title, None)
        self.assertEqual(description, None)


    def test_get_extra_titles(self):
        data = '# title Hello world\n# description Some description for out task\n# tag set, list'
        title, description = get_titles(data)
        self.assertEqual(title, 'Hello world')
        self.assertEqual(description, 'Some description for out task')


    def test_prepare_data(self):
        data = '''# title Hello world\n# description Some description for out task\n#<!---end--->print("Hello world")'''
        descr, code = prepare_data(data)
        self.assertEqual(code, '''print("Hello world")''')

    def test_prepare_empty_data(self):
        data = ""
        descr, code = prepare_data(data)
        self.assertEqual(code, "")
        self.assertEqual(descr, "")

    def test_add_new_data(self):
        new_data = '''# title Print Hello\n# description Напечатать на экран Hello!\n#<!---end--->\ndef print_hello():\nprint('Hello!')'''
        out = add_new_data(new_data)
        self.assertEqual(out, '''\n+ [Print Hello](#print-hello)\n## Print Hello\nНапечатать на экран Hello!\n\n\n<!---end--->\n```python\n\ndef print_hello():\nprint('Hello!')\n```''')


if __name__ == '__main__':
    unittest.main()
