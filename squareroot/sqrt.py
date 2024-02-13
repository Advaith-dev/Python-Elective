''''    square root algorithm by Sir Issac Newton
    z = 1 , initially the value of z is one
    let x be a positive floating point number 
    let y be the actual square root of x
    perform z = (z + x/ z) / 2, till the value for z becomes close to y
'''

num = float(input("Enter the positive number: "))

#square root calculated by direct method
py_estimate = num **(1/2)

#
z = 1

#Repeating until 7 decimal points become same
while "%0.7f" %  z != "%0.7f" %  py_estimate:
    z = (z + num / z) / 2

print("Python estimate: ",py_estimate,"Algorithm estimate: ",z)