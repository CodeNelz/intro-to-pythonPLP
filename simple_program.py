num1 = input("Please Enter number 1 :\n")
num2 = input("please Enter number 2 :\n")
operator = input("Please Enter the operator :\n")

if operator =="+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator =="/":
    result = num1 / num2
if operator == "*":
    result = num1 * num2

print(num1, operator, num2,"=", result )