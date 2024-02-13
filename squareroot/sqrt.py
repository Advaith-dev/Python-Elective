num = float(input("Enter the positive number: "))
py_estimate = num **(1/2)
z = 1

while "%0.7f" %  z != "%0.7f" %  py_estimate:
    z = (z + num / z) / 2

print("Python estimate: ",py_estimate,"Algorithm estimate: ",z)