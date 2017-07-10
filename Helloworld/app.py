"""Hello world"""

MESSAGE = "Hello world!!!"
print(MESSAGE)

print("\r\nIF:")
SUCCEED = True
if SUCCEED:
    print("True")
else:
    print("False")

print("\r\n多行语句:")
TOTAL = 1 + \
        2 + \
        3
print("TOTAL = ", TOTAL)

print("\r\nPrint换行和不换行输出")
print("a")
print("b")
print("-------")
print("a", end='')
print("b", end='')
