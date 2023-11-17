class Base:
    def printMe(self):
        print("Calling method printMe() in class Base.")

class Left(Base):
    def printMe(self):
        
        super().printMe()
        print("Calling method printMe() in class Left.")

class Right(Base):
    def printMe(self):
        
        super().printMe()
        print("Calling method printMe() in class Right.")

class Sub(Right, Left):
    def printMe(self):
        
        super().printMe()
        print("Calling method printMe() in class Sub.")

print(Sub.mro())
s = Sub()
s.printMe()

class Bus:
    def __init__(self, wheels, seats):
        self.__wheels = wheels
        self.__seats = seats
        
    def getInfo(self):
        return f"Number of Wheels: {self.__wheels}\nSeats: {self.__seats}"
    
class Boat:
    def __init__(self, screws, lifeJackets):
        self.__screws = screws
        self.__lifeJackets = lifeJackets
    
    def getInfo(self):
        return f"Screws: {self.__screws}\nLife Jackets: {self.__lifeJackets}"
    
class DuckBoat(Bus, Boat):
    def __init__(self, wheels, seats, screws, lifeJacket, mode):
        Bus.__init__(self, wheels, seats)
        Boat.__init__(self, screws, lifeJacket)
        self.__mode = mode
        
    def getInfo(self):
        return f"{Bus.getInfo(self)}\n{Boat.getInfo(self)}"
        

bus = Bus(4, 40)
print("== Bus ==")
print(bus.getInfo())
boat = Boat(1, 10)
print("== Boat ==")
print(boat.getInfo())
duckboat = DuckBoat(6, 20, 2, 25, "Bus")
print("== Duck Boat ==")
print(duckboat.getInfo())

class ScoreSheet:
    def __init__(self):
        self.__scores = {}
        
    def addScore(self, item, score):
        self.__scores[item]=score
        
    
    def getScore(self, item):
        return self.__scores[item]
    
    def getAverageScore(self):
        num_of_scores = 0
        total_score = 0
        for score in self.__scores:
            total_score += self.__scores[score]
            num_of_scores += 1
        total_score = total_score / num_of_scores
        return total_score
    
    

scoreSheet = ScoreSheet()
scoreSheet.addScore("OOP", 95)
scoreSheet.addScore("Database", 90)
scoreSheet.addScore("Network", 70)
print("Network Score:", scoreSheet.getScore("Network"))
print("OOP Score:", scoreSheet.getScore("OOP"))
print("Average Score:", scoreSheet.getAverageScore())