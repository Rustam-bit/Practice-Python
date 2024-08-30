str = (input().replace("!", "").replace(",", "").replace(".", "").replace("?", "").replace(";", "")
       .replace(":", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "")
       .replace("*", "").replace("(", "").replace(")", "").lower()).split()

b = {ch for ch in str if len(ch) >= 5 and len(set(ch)) >= 4 and str.count(ch) > 2}
for x in sorted(b):
    print(x)
