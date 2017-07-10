"""test exception"""

def divide(dividend, divisor):
    """divide"""
    result = None

    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Type error: division by 0.")
    except TypeError:
        # E.g., if b is a string
        print("Type error: division by '{0}'.".format(divisor))
    except Exception as err:
        # handle any other exception
        print("Error '{0}' occured. Arguments {1}.".format(err.message, err.args))
    else:
        # Excecutes if no exception occured
        print("No errors")
    finally:
        # Executes always
        if result is None:
            result = 0

    return result

if __name__ == "__main__":
    print(divide(1, 0))
    print(divide(12, 3))
    print(divide("12", "3"))
