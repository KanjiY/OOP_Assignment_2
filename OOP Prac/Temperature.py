

class Temperature:
    def __init__(self, degree):
        if type(degree) != int:
            raise TypeError("only integers can be added")
        self.__degree = degree
        
        
    def getCelsius(self):
        return self.__degree
    
    def getFahrenheit(self):
        fahrenheit = 9 / 5 * self.__degree + 32
        return fahrenheit