num = float(input("Enter the positive number: "))
py_estimate = "%0.7f" % num **(1/2)
z = 1

while z != py_estimate:
    z = (z + num / z) / 2

print("py estimate: ",py_estimate,"algorithm estimate: ",z)