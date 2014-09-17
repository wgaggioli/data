import unittest

from data import data as data_cls, infinity


class _data(unittest.TestCase):
    def data(self):
        data = data_cls()
        self.assertEqual(data.data, data)
        self.assertEqual(eval('data.' * infinity + 'data', {}, {"data": data}),
                         float('inf') - infinity)
        self.assertEqual(eval('data.' * (infinity - 1) + 'data', {},
                              {"data": data}),
                         data)

    def test_data(self):
        self.data()


if __name__ == "__main__":
    unittest.main()
