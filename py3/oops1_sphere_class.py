class Sphere():

    Pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * self.Pi * self.radius * self.radius

    def volume(self):
        return 4/3 * self.Pi * self.radius * self.radius * self.radius 

s = Sphere(1)
print(s.surface_area())
print(s.volume())