from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    a = []
    for i, j in zip_longest(values_list_1, values_list_2):
        if i == None:
            i = 1
        if j == None:
            j = 1
        a.append((i, j))
    return a


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
