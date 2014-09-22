from collections import defaultdict
import inspect
import time
import opcode
import dis


infinity = 5


LOAD_ATTR = opcode.opmap['LOAD_ATTR']


class Infinidata(float):
	
	def __new__(cls, *args):
		return float.__new__(cls, 'inf')
	
	@property
	def data(self):
		return self


class data(object):
	
	def __init__(self):
		self._infinidata = Infinidata('your mom')
	
	def _get_data(self):
		count = 0
		frame = inspect.currentframe().f_back
		print '#', frame.f_code
		dis.disco(frame.f_code, frame.f_lasti)
		last_op = None
		try:
			co = frame.f_code
			code = co.co_code
			i = 0
			n = min(len(code), frame.f_lasti + 1)
			extended_arg = 0
			while i < n:
				op = ord(code[i])
				print opcode.opname[op].ljust(20),
				i = i+1
				if op >= opcode.HAVE_ARGUMENT:
					oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
					i = i+2
					if op == opcode.EXTENDED_ARG:
						extended_arg = oparg*65536L
					if op in opcode.hasname:
						name = co.co_names[oparg]
						print name,
						if op == LOAD_ATTR and name == 'data':
							count += 1
							if i >= frame.f_lasti and count > infinity:
								print '#', count
								return self._infinidata
						elif op == opcode.opmap['LOAD_NAME']:
							count = 0
				if (
					op == opcode.opmap['LOAD_FAST']
					and last_op != opcode.opmap['STORE_FAST']
				):
					count = 0
				last_op = op
				print '#', count
		finally:
			del frame
			del co
			del code
		return self
	data = property(_get_data)


def _main():
	my_data = data()
	
	print 'simple 1', '-'*80
	print my_data.data.data.data.data.data
	
	print 'simple 2', '-'*80
	print my_data.data.data.data.data.data
	
	print '2 on one line', '-'*80
	print my_data.data.data.data.data.data, my_data.data.data.data.data.data
	
	end = time.time() + 0.2
	while time.time() < end:
		print 'eval', '-'*80
		print eval('my_data.data.data.data.data.data')
		time.sleep(0.1)


if __name__ == '__main__':
	#dis.dis(data._get_data)
	#dis.dis(_main)
	_main()
