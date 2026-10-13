#add a static method in problem 2 ,
#to greet the user with hello .


class Calculator: #class

    def __init__(self, n):
        self.n = n

    def square(self):
        print("Square =", self.n ** 2)

    def cube(self):
        print("Cube =", self.n ** 3)

    def square_root(self):
        print("Square root =", self.n ** 0.5)
    @staticmethod
    def hello():
        print ( "hello dear ")


num = int(input("Enter a number: "))

c = Calculator(num)
c.hello()
c.square()
c.cube()
c.square_root()
  