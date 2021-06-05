from collections import Counter

class FindSumPairs:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.counter = Counter(self.B)

    def add(self, i, val):
        self.counter[self.B[i]] -= 1
        self.counter[self.B[i] + val] += 1
        self.B[i] += val

    def count(self, target):
        return sum([self.counter[target - i] for i in self.A])
