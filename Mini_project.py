# Write oop class to handle the following scenarios:
#1- A user can create and view 2D coordinates (x, y).
#2- A user can calculate the distance between two coordinates.
#3- A user can find the distance from the origin (0, 0) to a coordinate.
#4- A user can check if the point lies on a given line.
#5- A user can find the distance between a 2D point and a line.

class Point:
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
# Answer to scenario 1
    def __str__(self):
        return '<{}/{}>'.format(self.x_cod, self.y_cod)
# Answer to scenario 2
    def euclidean_distance(self, other):
        return ((self.x_cod - other.x_cod) ** 2 + (self.y_cod - other.y_cod) ** 2) ** 0.5
# Answer to scenario 3
    def distance_from_origin(self):
        return ((self.x_cod ** 2 + self.y_cod ** 2) ** 0.5)
# Answer of scenario 4
class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return '{}x+{}y+{}=0'.format(self.A, self.B, self.C)
    def point_on_line(line, point):
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lie on the line"
# Answer to scenario 5
    def shortest_distance(line, point):
        return abs(line.A * point.x_cod + line.B * point.y_cod + line.C) / ((line.A ** 2 + line.B ** 2) ** 0.5)

# Object 1
p1 = Point(3,5)
p2 = Point(1,1)
p1.euclidean_distance(p2)

# Object 2
l1 = Line(2, 3, 4)
p1 = Point(3, 5)
l1.shortest_distance(p1)


# Print
print(p1)
print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())
print(l1)
print(p1)
print(Line.point_on_line(l1, p1))
print(l1.shortest_distance(p1))