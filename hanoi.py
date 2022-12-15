import sys
import argparse


class Stack:
    def __init__(self, name=''):
        self._name = name
        self._container = []

    def pop(self):
        return self._container.pop()

    def push(self, val):
        self._container.append(val)

    def __lt__(self, other):
        return self._name < other._name

    def __gt__(self, other):
        return self._name > other._name

    def __repr__(self):
        return 'Name {}: {}'.format(self._name, repr(self._container))


def SortedPrint(title, *args) -> None:
    sorted_out = sorted(args)
    print(title, sorted_out)


def hanoi(start: Stack, end: Stack, temp: Stack, n: int) -> None:
    if n == 1:
        end.push(start.pop())
    else:
        hanoi(start, temp, end, n - 1)
        SortedPrint('Step1', start, temp, end)
        hanoi(start, end, temp, 1)
        SortedPrint('Step2', start, temp, end)
        hanoi(temp, end, start, n - 1)
        SortedPrint('Step3', start, temp, end)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    args = parser.parse_args(sys.argv[1:])
    a = Stack('A')
    for i in range(args.n, 0, -1):
        a.push(i)
    b = Stack('B')
    c = Stack('C')
    hanoi(a, c, b, args.n)
    print('Final: {}, {}, {}'.format(a, b, c))
