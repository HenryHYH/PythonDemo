"""数据结构"""

LIST_A = [1, 2, 3]
LIST_B = [3, 4, 5]
print("A + B =", LIST_A + LIST_B)

LIST_C = [0 for i in range(5)]
print("C = ", LIST_C)

LIST_D = [i for i in range(0, 15)]
print("D =", LIST_D)
print("D[::2] =", LIST_D[::2])

TUPLE_A = (1, 2, 3)
TUPLE_B = (3, 4, 5)
print("A + B =", TUPLE_A + TUPLE_B)

DIC_A = {"A": "StrA", "B": "StrB", "B": "StrB2"}
print("A =", DIC_A)
print("A[A] = ", DIC_A["A"])
DIC_A["C"] = "StrC"
print("A =", DIC_A)
for k, v in DIC_A.items():
    print(k, "=", v)
