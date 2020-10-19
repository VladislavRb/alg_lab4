import overflow_chain_hash_table
import linear_probing_hash_table
import double_hash

import numpy as np
import matplotlib.pyplot as plt

from random import randint
from math import sqrt


def test_overflow_chain(keys_amount: int, keys_value_range: int, table_length: int):
    keys = [randint(1, keys_value_range) for i in range(keys_amount)]
    knut_constant = 0.5 * (sqrt(5) - 1)

    ht = overflow_chain_hash_table.HashTable(keys, knut_constant, table_length)
    ht.print()


def test_linear_probing(keys_amount: int, keys_value_range: int, table_length: int):
    keys = [randint(1, keys_value_range) for i in range(keys_amount)]
    knut_constant = 0.5 * (sqrt(5) - 1)

    ht = linear_probing_hash_table.HashTable(keys, knut_constant, table_length)
    ht.print()


def test_double_hash(keys_amount: int, keys_value_range: int, table_length: int):
    keys = [randint(1, keys_value_range) for i in range(keys_amount)]
    knut_constant = 0.5 * (sqrt(5) - 1)

    ht = double_hash.HashTable(keys, knut_constant, table_length)
    ht.print()


def personal_constant(constant: float, repetitions: int, keys_amount: int, keys_value_range: int, table_length: int):
    knut_constant = 0.5 * (sqrt(5) - 1)

    knut_const_is_better_cases = 0
    knut_const_is_worse_cases = 0

    for i in range(repetitions):
        keys = [randint(1, keys_value_range) for i in range(keys_amount)]

        knut_ht = overflow_chain_hash_table.HashTable(keys, knut_constant, table_length)
        ht = overflow_chain_hash_table.HashTable(keys, constant, table_length)

        if knut_ht.max_collision() <= ht.max_collision():
            knut_const_is_better_cases += 1
        else:
            knut_const_is_worse_cases += 1

        # ht.print()

    print("knut constant won:", knut_const_is_better_cases, " times")
    print("personal constant won:", knut_const_is_worse_cases, " times")


def get_average_collision_length(constant: float, keys_amount: int, keys_value_range: int, table_length: int, precision=100):
    max_collisions_array = []

    for precision_ind in range(precision):
        keys = [randint(1, keys_value_range) for i in range(keys_amount)]
        ht = overflow_chain_hash_table.HashTable(keys, constant, table_length)

        max_collisions_array.append(ht.max_collision())

    return np.average(max_collisions_array)


def plot_constant_efficiency_graph(min_constant: float, max_constant: float, keys_amount: int, keys_value_range: int,
                                   table_length: int, precision=100):
    knut_constant = 0.5 * (sqrt(5) - 1)

    step = 0.01
    n = int((max_constant - min_constant) / step)

    x = [min_constant + (max_constant - min_constant) * i / n for i in range(n)]
    y = [get_average_collision_length(consant, keys_amount, keys_value_range, table_length, precision) for consant in x]

    best_collision = min(y)
    best_collision_index = y.index(best_collision)
    best_constant = x[best_collision_index]

    plt.plot(x, y)
    plt.plot([knut_constant, knut_constant], [0, 5])

    plt.plot([best_constant, best_constant], [0, 5])

    plt.show()


plot_constant_efficiency_graph(0, 5, 10, 100, 15)

# personal_constant(0.55, 5, 10, 100, 10)
