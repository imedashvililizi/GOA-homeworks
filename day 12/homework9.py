"""შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება).
მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას"""

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
opeeration = input("what operation do you want to perform :")
if opeeration == "-":
    print(num1 + num2)
if opeeration == "-":
    print(num1 - num2)
if opeeration == "*":
    print(num1 * num2)
if opeeration == "/":
    print(num1 / num2)

