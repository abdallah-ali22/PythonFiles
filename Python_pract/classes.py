class Point:
    default_color = "Red"
    # Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        # print("draw function")
        print(f"Point is ({self.x},{self.y})")
    
    # magic method eq for check equality
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self,other):
        # return Point(self.x+other.x,self.y+other.y) => this is default
        return (self.x+other.x,self.y+other.y)

         
class Animal:
    def __init__(self,age):
        self.age = age
    def eat(self):
        print("Animal eat")

class Mammal(Animal):
    def walk(self):
        print("Mammal walk")

class Fish(Mammal):
    def swim(self):
        print("Fish swim")


mammal1 = Mammal(2)
fish1 = Fish(1)
print(fish1.age)
fish1.eat()
mammal1.eat()
# point1 = Point(2,3)
# point2 = Point(1,2)
# print(point1 == point2) # the result is false because == refer to the address (reference)
# print(point1 > point2)
# print(point1 + point2)


# point1 = Point(2,3)
# point1.draw()
# print(f"Obj 1 color is {point1.default_color}")
# point1.default_color = "Yellow"
# print(f"Obj 1 color after change is {point1.default_color}")
# point1.new_attrb = "test"

# point2 = Point(6,7)
# point2.draw()
# print(f"Obj 2 color is {point1.default_color}")
# print(f"obj2 new attrb is {point2.new_attrb}")

# print(type(point1))
# print(isinstance(point1,int))
