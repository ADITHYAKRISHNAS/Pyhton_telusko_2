
class Computer:

    def config(self):

        print("i5, 16gb, 1TB")


com1 = Computer()

com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()

a = 5
a.bit_length()

##################################

class Computer:
    def __init__(self, cpu, ram):
        # print("in init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Ryzen 5", 8)

com1.config()
com2.config()

