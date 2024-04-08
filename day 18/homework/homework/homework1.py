"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.
"""
list = []

for i in range(4):
    num = int(input("enter number :"))
    list.append(num)

result = 0


for num in list:
    result = result + num

print(result)
