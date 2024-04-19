"""შექმენით ფუნქცია სახელად num_divisors. ამ სიას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი მთელი რიცხვი. 
თქვენი დავალებაა, რომ დააბრუნოთ სია, სადაც იქნება ამ რიცხვის ყველა გამყოფი. Test case: 20 -> [1, 2, 4, 5, 10, 20]
"""
def num_divisors(number):

    list = []
num1 = int(input("enter number: "))
for i in range(num1):
    if  num1 // num1 == 0:
        list.append(num1)
num_divisors(num1)