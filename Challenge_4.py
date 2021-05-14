from time import sleep
import turtle
from sys import exit
print("Starting up...")
sleep(2)
name = input("What is you name? > ")
print("Hello,", name,)
if name == "butt jim":
    print("Stop appearing!!!!!!!!!!!")
    sleep(2)
    print("ShUtTiNg DoWn?.!")
    sleep(5)
    exit(["ERR_BUTT_JIM"])
decimal = float(input("Input the percent in decimal form > "))
float_decimal = float(decimal)
price = float(input("Input the original price > "))
float_price = float(price)
of = float_price * float_decimal
print("You may:")
print("1. Calculate Sales Tax")
print("2. Calculate Discount")
print("Type 1 or 2")
sleep(2)
choice = input("Which one? > ")
if choice == "1":
    sales_tax = float_price + of
    print("The final price is:", sales_tax)
elif choice == "2":
    discount = float_price - of
    print("Your final price is:", discount)
else:
    print("accepted inputs are 1 and 2")
    sleep(2)
    print("Bye")
    sleep(3)
    exit(["ERR_WRONG_INPUT"])
turtle.forward(500)
turtle.backward(500)
turtle.left(90)
turtle.forward(500)
turtle.backward(500)
turtle.left(90)
turtle.forward(500)
turtle.backward(500)
turtle.left(90)
turtle.forward(500)
turtle.backward(500)
del turtle