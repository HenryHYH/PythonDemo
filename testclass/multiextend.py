"""多继承"""

class Test1():
    """test1"""
    def print1(self):
        """print"""
        print("test1 print1")
    def print(self):
        """print"""
        print("test1 print")

class Test2():
    """test1"""
    def print1(self):
        """print"""
        print("test2 print1")
    def print(self):
        """print"""
        print("test2 print")

class Test(Test1, Test2):
    """test1"""
    def print(self):
        """print"""
        print("test print")

class Test3(Test2, Test1):
    """test1"""
    pass

obj = Test()
obj.print()
obj.print1()
obj3 = Test3()
obj3.print()
obj3.print1()