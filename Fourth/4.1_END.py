import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    a = [datetime.datetime.fromisoformat(date).month for date in dates]
    b = [i for i, j in Counter(a).most_common(n)]
    return b


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
