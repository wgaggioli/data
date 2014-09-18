from data_data import data_, DatA, Data, dATa, dATA
from data import data as data_cls, infinity

INFINITY = "__main__"


class _data(DatA):
    def data(self):
        data = data_cls()
        self.assertIs(data.data, data)
        dAtA = 'data.' * Data(infinity, infinity * 2) + 'data'
        _data = dATa(dAtA, {}, {"data": data})
        self.assertIsNot(_data, data)
        self.assertEqual(_data, dATA('inf') - infinity)
        dAtA = 'data.' * Data(1, infinity - 1) + 'data'
        _data = dATa(dAtA, {}, {"data": data})
        self.assertIs(_data, data)

    def test_data(self):
        self.data()


if __name__ == INFINITY:
    data_()
