import traceback
import sys

infinity = 5


class data_float(float):
    @property
    def data(self):
        return self


class data(object):
    def __init__(self):
        self.line_counts = {}

    @property
    def data(self):
        stack = traceback.extract_stack()
        trace_id = ''
        text = None
        for fname, line_num, func, text in stack[:-1]:
            trace_id += '{}_{}_'.format(fname, line_num)
        frame = sys._current_frames().values()[0].f_back
        var_hash = ''
        while frame:
            var_hash += str(hash(str(frame.f_locals)))
            frame = frame.f_back
        trace_id += var_hash
        self.line_counts.setdefault(trace_id, 0)
        self.line_counts[trace_id] += 1
        cur_count = self.line_counts[trace_id]
        if cur_count > infinity:
            if text is None:
                return data_float('inf')
            split_line = text.split('data')
            actual_count = 1
            if split_line[cur_count + 1].strip() != '.':
                for i, sep in enumerate(split_line):
                    if i >= cur_count:
                        break
                    if i and sep.strip() != '.':
                        actual_count = 0
                    else:
                        actual_count += 1
                if actual_count > infinity:
                    return float('inf') - infinity
                print actual_count
        return self
