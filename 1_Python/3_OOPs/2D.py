class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y
    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)
    def euclidean_distance(self,other):
        dist = round( ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5 , 3)
        return dist
    def distance_from_origin(self):
        return round( self.euclidean_distance(Point(0,0)) , 3)
    def point_lies_on_line(self,other):
        return (self.x_cod* other.A) + (self.y_cod * other.B) + other.C == 0
    
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):  
        return f"{self.A}x{self.B:+}y{self.C:+}=0"
    def line_shortest_distance_to_point(self , other):
        numenator = abs((self.A*other.x_cod)+(self.B*other.y_cod)+(self.C))
        denominator = (self.A**2 + self.B**2)**0.5
        return round(numenator/denominator , 3)


p1 = Point(2,4)
p2 = Point(5,4)
print(p1.euclidean_distance(p2))
print(p2.distance_from_origin())

l1 = Line(1,2,3)
print(l1)

print(p1.point_lies_on_line(Line(1,3,-14)))

dist1=Line(1,2,3).line_shortest_distance_to_point(Point(1,2))
print(dist1)

p3 = Point(3,9)
l2 = Line(4,5,6)
dist2 = l2.line_shortest_distance_to_point(p3)
print(dist2)
