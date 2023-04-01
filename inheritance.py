class A:

    def feature_1(self):
        print("Feature 1 working")

    def featuer_2(self):
        print("Feature 2 working")


class B(A):

    def feature_3(self):
        print("Feature 3 working")

    def featuer_4(self):
        print("Feature 4 working")

class C(B):

    def feature_5(self):
        print("Feature 5 working")


a1 = A()
b1 = B()
c1 = C()
a1.feature_1()
a1.featuer_2()

b1.featuer_3()
c1.feature_5()

