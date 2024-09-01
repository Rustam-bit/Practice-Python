class Dictionary:
   def __init__(self, dictionary):
       self.elem = dictionary

   def __call__(self, key):
       return self.elem.get(key)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)