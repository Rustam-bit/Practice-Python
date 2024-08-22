str = input()
print(str.count("!") + str.count("#") + str.count("@") + str.count("%"))
print(str.lower().replace("!", "").replace("%", "").replace("#", "").replace("@", ""))
