from collections import deque
from heapq import heappush, heappop

class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        return self._data.pop()

    def empty(self):
        return len(self._data) == 0

class Queue:
    def __init__(self):
        self._data = deque()

    def push(self, val):
        self._data.append(val)

    def pop(self):
        return self._data.popleft()

    def empty(self):
        return len(self._data) == 0


class PriorityQueue:
    def __init__(self):
        self._data = []

    def push(self, val):
        heappush(self._data, val)

    def pop(self):
        return heappop(self._data)

    def empty(self):
        return not self._data
