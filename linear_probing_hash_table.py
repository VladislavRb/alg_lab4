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
            hash_value = self.hash_function(elem)

            while self.cells[hash_value % self.M].value is not None:
                hash_value += 1

            self.cells[hash_value % self.M].value = elem

    def hash_function(self, k):
        kA = k * self.A
        return floor(self.M * (kA - floor(kA)))

    def print(self):
        for cell in self.cells:
            print(cell.hash, "-", cell.value)
