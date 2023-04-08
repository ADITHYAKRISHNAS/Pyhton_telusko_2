from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        # print("running")
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class Whiteboard:
    def write(self):
        print("its writing")

class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()


# com = Computer()
com1 = Laptop()
com2 = Whiteboard()
# com.process()
# com1.process()
prog1 = Programmer()
# prog1.work(com1)
prog1.work(com2)

# com1.process()
