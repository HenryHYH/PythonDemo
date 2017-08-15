"""限制实例的属性"""

class Student(object):
    """Student"""
    __slots__ = ("name", "age")

if __name__ == "__main__":
    obj = Student()
    obj.name = "Name"
    obj.age = 1
    obj.other_field = "other_field"