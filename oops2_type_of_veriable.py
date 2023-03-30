class Car:

    whaeels = 4

    def __init__(self) -> None:
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

Car.whaeels = 5

print(c1.com, c1.mil, c1.whaeels)
print(c2.com, c2.mil,c2.whaeels)

