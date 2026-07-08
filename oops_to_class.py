class Square:

    final = 1

    def __init__(self, num):
        self.num = num

    def dSquare(self):
        self.final = (self.num * self.num)

    def __str__(self):
        return f"The square of {self.num} is {self.final}"
    


newSquare = Square(3)

newSquare.dSquare()

print(newSquare)