""""class user"""

class User:
    """user"""
    def __init__(self, name):
        self.Name = name

    Id = 1
    def ShowInfo(self):
        """Show"""
        return "user"

if __name__ == "__main__":
    entity = User("Henry")
    print("Id =", entity.Id)
    print("Name =", entity.Name)
    print("ShowInfo =", entity.ShowInfo())
