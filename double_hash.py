from math import floor


class Cell:
    def __init__(self, hash_value: int):
        self.hash = hash_value
        self.value = None


class HashTable:
    def __init__(self, arr: list, multiplicative_constant: float, table_size: int):
        self.M = table_size
        self.A = multiplicative_constant
        self.cells = [Cell(i) for i in range(self.M)]

        for elem in arr:
            i = 0

            while self.cells[self.combined_hash(elem, i)].value:
                i += 1

            self.cells[self.combined_hash(elem, i)].value = elem

    def h1(self, k):
        kA = k * self.A
        return floor(self.M * (kA - floor(kA)))

    def h2(self, k):
        kA = k * self.A / 2
        return floor(self.M * (kA - floor(kA)))

    def combined_hash(self, k, i):
        return (self.h1(k) + i * self.h2(k)) % self.M

    def print(self):
        for cell in self.cells:
            print(cell.hash, "-", cell.value)
