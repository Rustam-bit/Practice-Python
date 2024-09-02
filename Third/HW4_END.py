class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


# YOUR CODE HERE


class CalculatePerimeterMixin(Rectangle):
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)


# YOUR CODE HERE


class SquareWithMixin(CalculatePerimeterMixin, Square):
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    # YOUR CODE HERE

    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()

    # YOUR CODE HERE

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()


# YOUR CODE HERE

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
