class Circle:
   pi = 3.14

   def calculate_area(self, radius):
       return radius * self.pi * radius

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)