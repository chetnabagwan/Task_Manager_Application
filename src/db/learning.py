# x = 7,8,9
import timeit
# print(x)
# print(type(x))
# print(x==7,8,9)
a="""
def a():
    print("Hello",end="")
    print("World")"""

b="""def b():
    print("Hello",end="",flush = True)
    print("World")"""

print(timeit.timeit(stmt=a,number=1))
print(timeit.timeit(stmt=b,number=1))

# print("Hello, World", flush=True)

