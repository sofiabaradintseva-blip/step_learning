##try:
##    a = int(input("Please enter number:"))
##    result = 10 / a
##    print(result)
##except ValueError:
##    print("It's not a number")
##except ZeroDivisionError:
##    print("Division by zero not permitted")

##def  check_age(age):
##    if age < 18:
##        raise ValueError("Deny")
##    return age
##
##print(check_age(12))

##try:
##    x = int("abc")
##except (ValueError, TypeError):
##    print("Value or type error")

def withdrow(balance, amount):
    if amount > balance:
        raise ValueError("Low balance")
    return balance - amount

#try:
#    print(withdrow(100, 200))
#except ValueError as e:
#   print(e)
import math
def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def calc(x, y, operation):
    if not is_number(x):
        raise ValueError("A should be a number")
    if not is_number(y):
        raise ValueError("B should be a number")
    if operation == "/" and y == 0:
        raise ValueError("Devide by zero")
    if operation not in ("+", "-", "*", "/"):
        raise ValueError("Bad operation")
    if operation == "+":
        return x + y
    if operation == "-":
        return x - y
    if operation == "*":
        return x * y
    if operation == "/":
        return x / y

a = int(input("Please enter number: "))
b = int(input("Please enter number: "))
op = input("Please input operation(+ or - or * or /)")
try:
    result = calc(a, b, op)
except ValueError as e:
    print(e)
else:
 print("Result: ", result)
