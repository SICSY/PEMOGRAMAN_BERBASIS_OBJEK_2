class Class1:
    def m(self):
        print('in Class1')
class Class2(Class1):
    def m(self):
        print("in Class2")
        Class1.m(self)
class Class3(Class1):
    def m(self):
        print('in Class3')
        Class1.m(self)
class Class4(Class1):
    def m(self):
        print('in Class4')
        Class2.m(self)
        Class3.m(self)
obj = Class4()
obj.m()
