class Rectangle:
    def __init__(self , l , b):
        self.__length = l
        self.__width = b
    
    def __perimeter(self):
        perimeter = 2 * (self.__length * self.__width)
        return perimeter
    def __area(self):
        area = self.__length * self.__width
        return area
    def display(self):
        print("length " , self.__length)
        print("width " , self.__width)
        print("Perimeter " , self.__perimeter())
        print("Area " , self.__area())
        