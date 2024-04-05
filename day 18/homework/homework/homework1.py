"""მომხმარებელს შემოატანინეთ ხუთი რიცხვი და ყველა შეიტანეთ სიაში. თქვენი დავალებაა, რომ დაბეჭდოთ ამ სიის ჯამი, არ გამოიყენოთ sum მეთოდი.
"""
list = []

for i in range(5):
    list1=int(input("enter number"))
    list.append(list1)
print(list[0] + list[1] + list[2] + list[3] + list[4])