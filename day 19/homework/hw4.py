"""სიების შეერთება: დაწერეთ ალგორითმი, რომელიც მიიღებს ორ რიცხვთა სიას, გააერთიანებს მათ ერთ სიაში და ამ სახით დაბეჭდავს."""

list0 = []

for i in range(3):
    num0 = int(input("enter number :"))
    list0.append(num0)


list1 = []

for i in range(2):
    num1 = int(input("enter number :"))
    list1.append(num1)


list2 = list0 + list1
print(list2)