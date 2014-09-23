from datetime import datetime, timedelta
from data_data import data_, DatA, Data, dATa, dATA
from data import data as data_cls, infinity

INFINITY = "__main__"


class TestWillData(DatA):
    def data(self):
        data = data_cls()
        self.assertIs(data.data, data)
        dAtA = 'data.' * Data(infinity + 1, infinity * 2) + 'data'
        _data = dATa(dAtA, {}, {"data": data})
        self.assertIsNot(_data, data)
        self.assertEqual(_data, dATA('inf') - infinity)
        dAtA = 'data.' * Data(1, infinity) + 'data'
        _data = dATa(dAtA, {}, {"data": data})
        self.assertIs(_data, data)
        dAtA = 'data.' * Data(int(infinity / 2) + infinity % 2, infinity) + \
            'data'
        dAtA = dAtA + ',' + dAtA
        data1, data2 = dATa(dAtA, {}, {"data": data})
        self.assertIs(data1, data)
        self.assertIs(data2, data)
        datum = datetime.utcnow() + timedelta(seconds=1)
        dAtA = 'data.' * Data(1, infinity) + 'data'
        while datetime.utcnow() < datum:
            self.assertIs(dATa(dAtA, {}, {"data": data}), data)
        tricky_data = data.data.data.data\
            .data.data.data.data
        self.assertEqual(tricky_data, dATA('inf') - infinity)
        data3, data4 = data.data.data.data, data.data\
            .data.data
        self.assertIs(data3, data)
        self.assertIs(data4, data)

        data_d = getattr(data, 'data')
        self.assertIs(data_d, data)
        data_inf = getattr(
            getattr(
                getattr(
                    getattr(
                        getattr(
                            getattr(getattr(data, 'data'), 'data'),
                            'data'),
                        'data'),
                    'data'),
                'data'),
            'data')
        self.assertIs(data_inf, dATA('inf') - infinity)

    def test_data(self):
        self.data()


class TestTannersWay(object):

    def test_generator(self):
        start_offset = 2
        for n in xrange(start_offset, infinity+start_offset):
            test_data = data_cls()
            yield self.make_data_func('new', test_data, n, test_data, float('inf'))
        for n in xrange(infinity+start_offset, infinity+2+start_offset):
            test_data = data_cls()
            yield self.make_data_func('new', test_data, n, float('inf'), test_data)
        test_data = data_cls()
        for n in xrange(start_offset, infinity+start_offset):
            yield self.make_data_func('existing', test_data, n, test_data, float('inf'))
        for n in xrange(infinity+start_offset, infinity+2+start_offset):
            yield self.make_data_func('existing', test_data, n, float('inf'), test_data)
        
        
        for n in xrange(start_offset, infinity+start_offset):
            test_data = data_cls()
            yield self.make_data_func('new', test_data, n, (test_data,test_data), (float('inf'),float('inf')), times=2)
        
        test_data = data_cls()
        inf_expression = 'data.{}'.format('.'.join(['data']*(infinity+1)))
        yield (self.assert_data,
                test_data,
                'data.data,{}'.format(inf_expression),
                (test_data, float('inf')),
                (float('inf'), test_data),
                'data^1 then data^{} in one statement'.format(infinity+1))
        yield (self.assert_data,
               test_data,
               '{},data.data'.format(inf_expression),
               (float('inf'), test_data),
               (test_data, float('inf')),
               'data^{} then data^1 in one statement'.format(infinity+1))

    def make_data_func(self, data_func_label, test_data, n, expected_data,
                       unexpected_data, times=1):
        data_n_tuple = ('data',)*n
        data_expression = ', '.join(['.'.join(data_n_tuple)]*times)
        data_expression_label = '{} {} data^{} {} times ( {} while infinity={} )'.format(
            data_func_label, test_data, n-1, times, data_expression, infinity)
        data_test = lambda: self.assert_data(test_data, data_expression,
            expected_data, unexpected_data, data_expression_label)
        data_test.description = (
            'Test {} is or equals {} while not being or being equal to {}'
        ).format(data_expression_label, expected_data, unexpected_data)
        data_test.compat_func_name = data_test.description
        return data_test
    
    def assert_data(self, test_data, data_expression, expected_data, unexpected_data,
                    data_expression_label):
        evaluated_data = eval(data_expression, {}, {'data': test_data})
        assert (
            evaluated_data is expected_data
            or evaluated_data == expected_data
        ), "{} should be the same or equal to {} but is {}".format(
                data_expression_label, expected_data, evaluated_data)
        assert (
            evaluated_data is not unexpected_data
            and evaluated_data != unexpected_data
        ), "{} should NOT be the same or equal to {} but is {}".format(
                data_expression_label, unexpected_data, evaluated_data)


if __name__ == INFINITY:
    data_()
