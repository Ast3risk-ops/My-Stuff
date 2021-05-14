# A "computer" in Python (idea from Phin).
from turtle import Turtle
from time import sleep
from sys import exit
def computer():
    print("Hello, I am the computer")
    sleep(1)
    print("You can...")
    sleep(1)
    print("1. Check your emails")
    print("2. Write something")
    print("3. Check your bank account")
    print("4. Text your friend")
    print("5. Look at the turtle")
    print("6. Use the calculator")
    print("7. Calculate discount or sales tax")
    print("8. Look at some squares")
    print("9. See a smiley face")
    print("10. See 3 shapes")
    print("11. See a train")
    print("12. See an alien")
    print("13. Roll the dice")
    print("Type: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13")
    choice = input("What would you like to do? > ")
    if choice == "1":
        print("Checking for new mail...")
        sleep(5)
        print("YOU HAVE MAIL!!!!!!!!!!!!!!!!!!!!!!!!!")
        sleep(1)
        print("loading mail...")
        sleep(3)
        print("It says...")
        sleep(1)
        print("Hello from the gas comapny,")
        print("We would just like to say that there is a gas leak in your house at the moment")
        print("A fire could occur if you do not turn off the gas")
        print("Please call us at 1-800-URE-DOOM to fix the leak")
        sleep(3)
        print("End of new mail")
        sleep(10)
    elif choice == "2":
        text = input("Type something... > ")
        if text == "butt jim":
            def buttjim():
                print("Just stop...")
                sleep(3)
                exit(["ERR_BUTT_JIM"])
            buttjim()

        print(text)
        sleep(3)
    elif choice == "3":
        print("You had $18000000000000000000000000000000000000000000000000000000000")
        sleep(2)
        print("But now, because of a grease fire and then a gas fire and then an explosion and bills at your mansion,")
        sleep(1)
        print("You now have...")
        sleep(3)
        print("Drumroll please...")
        sleep(5)
        print("$0")
        sleep(3)
    elif choice == "4":
        print("Contacting friend...")
        sleep(3)
        input("Would you like to text you friend: I pirate video games? > ")
        print("Texting...")
        sleep(1)
        print("Your friend has responded")
        sleep(1)
        input("Would you like to see their response? > ")
        sleep(1)
        print("Their response is...")
        sleep(2)
        print("I have contacted the authorities and you will be arrested")
        print("Run the script again to go back")
    elif choice == "5":
        turtle = Turtle()
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
        sleep(3)
        print("Run the script again to go back")
        del turtle
    elif choice == "6":
        import Challenge_3.py
    elif choice == "7":
        import Challenge_4.py
    elif choice == "8":
        import sqaure.py
    elif choice == "9":
        import smileyface.py
    elif choice == "10":
        import loop.py
    elif choice == "11":
        import challenge_8.py
    elif choice == "12":
        import tk_alien.py
    elif choice == "13":
        import dice.py
computer()
computer()
computer()
computer()
computer()