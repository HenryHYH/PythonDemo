"""String"""

VAL_A = "Hello"
VAL_B = "Python"

print("a + b =", VAL_A + VAL_B)
print("a * 2 =", VAL_A * 2)
print("a[1] =", VAL_A[1])
print("a[1:4] =", VAL_A[1:4])
print("a[1:] =", VAL_A[1:])
print("a[:4] =", VAL_A[:4])

print("M in a =", "H" in VAL_A)
print("Z not in b =", "Z" not in VAL_B)

print(r"\n")

print("Str = %s, Num = %d" % ('Str', 10))

STR_MULTI_LINE = """INSERT INTO tb (
    Name
)
VALUES (
    'Henry'
)
"""
print(STR_MULTI_LINE)
