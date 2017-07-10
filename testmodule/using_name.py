"""module using_name"""

def print_impl():
    """print"""
    if __name__ == "__main__":
        print("SELF")
    else:
        print("OTHER")

if __name__ == "__main__":
    print_impl()
