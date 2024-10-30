#!/usr/bin/env python3


class CountedIterator():
	def __init__(self, some_iterable):
		self.iterator = iter(some_iterable)
		self.count = 0

	def get_count(self):
		return self.count

	def __next__(self):
		item = self.iterator.__next__()
		self.count += 1
		return item
			
