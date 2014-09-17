import unittest

from data import data as data_cls, infinity


class _data(unittest.TestCase):
    def data(self):
        data = data_cls()
        self.assertIs(data.data, data)
        self.assertIs(eval('data.' * infinity + 'data', {}, {"data": data}),
                      float('inf') - infinity)
        self.assertIs(eval('data.' * (infinity - 1) + 'data', {},
                           {"data": data}),
                      data)

    def test_data(self):
        self.data()


if __name__ == "__main__":
    unittest.main()
