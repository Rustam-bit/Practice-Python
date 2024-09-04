from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
   d_dict = defaultdict(list)
   for s,v in specializations:
      d_dict[s].append(v)
   return dict(d_dict)


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)