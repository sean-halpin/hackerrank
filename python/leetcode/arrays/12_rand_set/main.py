import random

class RandomizedSet:

    def __init__(self):
        self.rSet = set()

    def insert(self, val: int) -> bool:
        if val in self.rSet:
            return False
        self.rSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rSet:
            return False
        self.rSet.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.rSet))
        