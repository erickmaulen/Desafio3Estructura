import heapq

class ColaPrioridad:
	def __init__(self):
		self._cola = []
		self._indice = 0

	def __len__(self):
		return len(self._cola)
		
	def push(self, elemento, prioridad):
		heapq.heappush(self._cola, (-prioridad, elemento))
		self._indice += 1
		
	def pop(self):
		return heapq.heappop(self._cola)[-1]

	def as_list(self):
		return list(self._cola)