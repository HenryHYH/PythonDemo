"""继承"""


#类定义
class People:
    """People"""

    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        """speak"""
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


#单继承示例
class Student(People):
    """"Student"""

    grade = ''

    def __init__(self, n, a, w, g):
        #调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


peo = People(10, 60, 3)
peo.speak()
stu = Student('ken', 10, 60, 3)
stu.speak()
