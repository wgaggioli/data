import traceback

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
        filename, line_num, func, text = stack[-2]
        simple_mode = False
        if text is None:
            simple_mode = True
            filename, line_num, func, text = stack[-3]
        self.line_counts.setdefault(filename, {}).setdefault(line_num, 0)
        self.line_counts[filename][line_num] += 1
        cur_count = self.line_counts[filename][line_num]
        if cur_count > infinity:
            if simple_mode:
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
