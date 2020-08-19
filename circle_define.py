def circle_area(x):
    a = x*x*3.14
    return a
def circle_circum(x):
    b = x*2*3.14
    return b
c = int(input("半徑:"))
print("面積:",circle_area(c))
print("周長:",circle_circum(c))
