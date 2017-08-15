"""属性"""

class Student(object):
    """Student"""

    @property
    def name(self):
        """getter"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

if __name__ == "__main__":
    obj = Student()
    obj.name = "Henry"
    print(obj.name)
