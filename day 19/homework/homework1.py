"""ნამრავლის გამოთვლა: დაწერეთ ალგორითმი, რომელიც დაბეჭდავს სიის ყველა ელემენტის ნამრავლს."""

list = []

for i in range(4):
    num = int(input("enter number :"))
    list.append(num)

result = 0


for num in list:
    result = result * num

print(result)



