""" შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე.
 გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს"""

num = 5

num1 = int(input("guess the number 1-10: "))

while num !=num1:
    print("try again")
    num1 =num1
if num == num1:
    print("correct")