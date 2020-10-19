from math import floor


class Cell:
    def __init__(self, hash_value: int):
        self.hash_value = hash_value
        self.hash_chain = []

    def insert_value_into_chain(self, new_value: int):
        value_insert_index = insert_index(self.hash_chain, new_value)
        self.hash_chain.insert(value_insert_index, new_value)


class HashTable:
    def __init__(self, arr: list, multiplicative_constant: float, table_size: int):
        self.M = table_size
        self.A = multiplicative_constant
        self.cells = [Cell(i) for i in range(self.M)]

        for elem in arr:
            hash_value = self.hash_function(elem)
            self.cells[hash_value].insert_value_into_chain(elem)

    def hash_function(self, k):
        kA = k * self.A
        return floor(self.M * (kA - floor(kA)))

    def print(self):
        for cell in self.cells:
            print(cell.hash_value, "-", *cell.hash_chain)

    def max_collision(self):
        return max([len(cell.hash_chain) for cell in self.cells])


def insert_index(cell_array: list, new_elem: int, start_index=0):
    if not len(cell_array):
        return start_index
    elif len(cell_array) == 1:
        return start_index + (0 if new_elem < cell_array[0] else 1)
    else:
        sep = int(len(cell_array) / 2)

        if cell_array[sep] > new_elem:
            return insert_index(cell_array[:sep], new_elem, start_index)
        else:
            return insert_index(cell_array[sep:], new_elem, start_index + sep)
