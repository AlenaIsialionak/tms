class Circle:

    def __init__(self, r):
        self.r = r


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        print(f'Point: {self.x}, {self.y}')


circle1 = Circle(int(input()))
circle2 = Circle(int(input()))
if circle1.r - circle2.r == 0:
    dot = Point(0, 0)
    dot.point()
else:
    print(abs(circle1.r - circle2.r))
