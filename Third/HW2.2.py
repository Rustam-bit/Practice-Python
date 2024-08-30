import math


class Pendulum:
   g = 10
   pi = 3.14

   @classmethod
   def calculate_period(cls, length):
       return 2 * cls.pi * math.sqrt(length/cls.g)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)