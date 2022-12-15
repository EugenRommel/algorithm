import random

from structures import Stack, Queue, PriorityQueue

class State:
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    MARK = '*'


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "({},{})".format(self.x, self.y)



class Node:
    def __init__(self, location, parent=None, heuristic=0):
        self.location = location
        self.parent = parent
        self.heuristic = heuristic

    def get_path(self):
        path_to_end = [self.location]
        cur_node = self.parent
        while cur_node:
            path_to_end.append(cur_node.location)
            cur_node = cur_node.parent
        path_to_end.reverse()
        return path_to_end

    def __repr__(self):
        return "{} -> {}".format(self.location, self.parent.location)

    def __lt__(self, other):
        return self.heuristic < other.heuristic


class Maze:
    def __init__(self, rows, columns, sparse=0.1,
                 start=Location(0, 0),
                 goal=Location(9, 9)):
        self._row = rows
        self._col = columns
        self._start = start
        self._goal = goal
        self._data = [[State.EMPTY for j in range(columns)] for i in range(rows)]
        self.fill(sparse)
        self._data[start.x][start.y] = State.START
        self._data[goal.x][goal.y] = State.GOAL

    def fill(self, sparse):
        while self.current_sparse() < sparse:
            fill_row = random.randint(0, self._row - 1)
            fill_col = random.randint(0, self._col - 1)
            fill_loc = Location(fill_row, fill_col)
            if fill_loc != self._start and fill_loc != self._goal:
                self._data[fill_row][fill_col] = State.BLOCKED

    def current_sparse(self):
        blocked_num = 0
        for row in self._data:
            for col in row:
                if col == State.BLOCKED:
                    blocked_num += 1
        return blocked_num / (self._row * self._col)

    def get_successors(self, loc):
        successors = []
        if loc.x + 1 < self._row and \
                self._data[loc.x + 1][loc.y] != State.BLOCKED:
            successors.append(Location(loc.x + 1, loc.y))
        if loc.x - 1 >= 0 and \
                self._data[loc.x - 1][loc.y] != State.BLOCKED:
            successors.append(Location(loc.x - 1, loc.y))
        if loc.y + 1 < self._col and \
                self._data[loc.x][loc.y + 1] != State.BLOCKED:
            successors.append(Location(loc.x, loc.y + 1))
        if loc.y - 1 >= 0 and \
                self._data[loc.x][loc.y - 1] != State.BLOCKED:
            successors.append(Location(loc.x, loc.y - 1))
        return successors

    def dfs(self):
        frontier = Stack()
        frontier.push(Node(self._start))
        explored = set()
        while not frontier.empty():
            cur_node = frontier.pop()
            if cur_node.location == self._goal:
                return cur_node

            successors = self.get_successors(cur_node.location)
            for loc in successors:
                if loc not in explored:
                    frontier.push(Node(loc, cur_node))
                    explored.add(loc)
        return None

    def bfs(self):
        frontier = Queue()
        frontier.push(Node(self._start))
        explored = set()
        while not frontier.empty():
            cur_node = frontier.pop()
            if cur_node.location == self._goal:
                return cur_node

            successors = self.get_successors(cur_node.location)
            for loc in successors:
                if loc not in explored:
                    frontier.push(Node(loc, cur_node))
                    explored.add(loc)
        return None

    def heuristic(self, location):
        x = abs(location.x - self._goal.x)
        y = abs(location.y - self._goal.y)
        return x + y

    def astar(self):
        frontier = PriorityQueue()
        frontier.push(Node(self._start))
        explored = {self._start: 0}
        while not frontier.empty():
            cur_node = frontier.pop()
            if cur_node.location == self._goal:
                return cur_node

            successors = self.get_successors(cur_node.location)
            new_cost = explored[cur_node.location] + 1
            for suc in successors:
                if suc not in explored or explored[suc] > new_cost:
                    frontier.push(Node(suc, cur_node, self.heuristic(suc)))
                    explored[suc] = new_cost
        return None

    def clear_marks(self):
        for r in self._data:
            for i in range(len(r)):
                if r[i] == State.MARK:
                    r[i] = State.EMPTY

    def __repr__(self):
        out = ''
        for row in self._data:
            row_str = ''.join(row)
            out += row_str + '\n'
        return out


if __name__ == "__main__":
    m = Maze(20, 20, 0.2, Location(0, 0), Location(19, 19))
    node = m.dfs()
    if node:
        path = node.get_path()
        for loc in path:
            if loc != m._start and loc != m._goal:
                m._data[loc.x][loc.y] = State.MARK
        print(m)
    else:
        print('No path found')
    m.clear_marks()
    node = m.bfs()
    if node:
        path = node.get_path()
        for loc in path:
            if loc != m._start and loc != m._goal:
                m._data[loc.x][loc.y] = State.MARK
        print(m)
    else:
        print('No path found')
    m.clear_marks()
    node = m.astar()
    if node:
        path = node.get_path()
        for loc in path:
            if loc != m._start and loc != m._goal:
                m._data[loc.x][loc.y] = State.MARK
        print(m)
    else:
        print('No path found')
