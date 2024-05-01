import sys
import random


nilai_dadu_set = frozenset({1, 2, 3, 4, 5, 6})

kocok_dadu = random.choice(list(nilai_dadu_set))

print(kocok_dadu)
