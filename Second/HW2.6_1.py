from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    return [i for i, el in sorted(d.items(), key=lambda x: x[1], reverse=True)]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

