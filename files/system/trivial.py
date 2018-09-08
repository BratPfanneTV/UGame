import ctypes

class trivial():
	def __init__(self):
		pass;
	def get_screensize(self, i, p=100):
		v = int(ctypes.windll.user32.GetSystemMetrics(i));
		v = v / 100;
		v = v * p;
		return int(v);
	def fsize(self, s):
		return (('MS', 'Sans', 'Serif'), s);