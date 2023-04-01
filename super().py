class A:
    def __init__(self):
        print("in A Init")

    def feature_1(self):
        print("Feature 1_A working")

    def featuer_2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        # super().__init__()
        print("in B Init")

    def feature_1(self):
        print("Feature 3_B working")

    def featuer_4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")


    def feat(self):
        super().featuer_2()

# a1 = A()

# b1 = B()

c1 = C()
c1.feature_1()
c1.feat()


