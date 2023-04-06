from structures import Queue

MAX_NUM = 3

class MState:
    def __init__(self):
        self.west_missionaries = MAX_NUM
        self.west_cannibals = MAX_NUM
        self.is_boat_west = True

    