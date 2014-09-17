import unittest

from data import data as data_cls, infinity


class _data(unittest.TestCase):
    def data(self):
        data = data_cls()
        self.assertIs(data.data, data)
        _data = eval('data.' * infinity + 'data', {}, {"data": data})
        self.assertIsNot(_data, data)
        self.assertEqual(_data, float('inf') - infinity)
        _data = eval('data.' * (infinity - 1) + 'data', {}, {"data": data})
        self.assertIs(_data, data)

    def test_data(self):
        self.data()


if __name__ == "__main__":
    unittest.main()
