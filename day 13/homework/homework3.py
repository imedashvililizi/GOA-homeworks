""" დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."""
A = 10
B = 8
C = 6
D = 4
F = 2

grade = int(input("flease enter your grade"))

if grade >= 9:
    print("Excellent!")
elif grade >= 7  :
    print("good job!")
elif grade >= 5:
    print("you passed")
elif grade >= 3:
    print("you can do better")
else:
    print("you failed")


