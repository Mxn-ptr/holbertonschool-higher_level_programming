#!/usr/bin/env python3


class VerboseList(list):
	
	def append(self, value):
		super().append(value)
		print(f"Added [{value}] to the list.")
	
	def extend(self, values):
		print(f"Extended the list with [{len(values)}] items.")
		super().extend(values)

	def remove(self, item):
		super().remove(item)
		print(f"Removed [{item}] from the list.")
	
	def pop(self, index=None):
		if index is not None:
			item = super().pop(index)
		else:
			item = super().pop()
		print(f"Popped [{item}] from the list.")
		return item
