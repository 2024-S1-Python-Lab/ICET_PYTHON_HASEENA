class Rectangle:
    def __init__(self,l,b):
        self.__length = l
        self.__breadth = b
        def getDimensions(self):
            return self.__length,self.__breadth
        def getArea(self):
            return self.__length * self.__breadth
        def __it__(self, other):
            if self.getArea() < other.getArea():
                return "1st rectangle is smaller"
            else:
                return "2nd rectangle is smaller"
length1 = int(input("enter the 1st rectangle length:"))
breadth1 = int(input("enter the 1st rectangle breadth:"))
ar1 = Rectangle(length1,breadth1)
length2 = int(input("enter the 2nd rectangle length:"))
breadth2 = int(input("enter the 2nd rectangle breadth:"))
ar2 = Rectangle(length2,breadth2)
print(f"area of first rectangle={ar1.getArea()}")
print(f"area of second rectangle={ar2.getArea()}")
print(ar1 < ar2)
            
            
        
