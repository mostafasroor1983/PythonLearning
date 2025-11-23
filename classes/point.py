class  Point:
    #Constructor to initialize point coordinates
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    #String representation of the point
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

p1 = Point(2, 3)
p1.x = 10
p1.move(4, 5)
print(p1)  # Output: Point(6, 8)



