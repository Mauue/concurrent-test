import requests
import time
from threading import Thread

class Request:
	def __init__(self, url):
		self.url = url
	
	def get(self, data=None, show_result=False):
		rst = requests.get(self.url, data=data)
		if show_result:
			print(rst)


class PressTest:
	def __init__(self, url)
		self.url = url
	
	def _cell_request(self):
		r = Request(self.url)
		r.get()

	def run(self, num=1)
		thread_list = []
		time_start = time.clock()
		for _ in range(num):
			t = Thread(targer=self._cell_request()
			t.start()
			thread_list.append(t)			
		for t in thread_list:
			t.join()
		time_end = time.clock()
		
		print("="*10 + "Result" + "="*10)
		print("total time", time_end-time_start)
		print("average time", (time_end-time_start)/num)


