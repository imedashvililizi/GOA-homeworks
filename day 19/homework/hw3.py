"""საშუალოს პოვნა: დაწერეთ ალგორითმი,
 რომელიც მიიღებს სიას და დააბრუნებს მის საშუალო არითმეტიკულს.
"""
numbers = []



for i in range(3):
    num = int(input("enter number :"))
    numbers.append(num)

result = 0


for num in numbers:
    result = result + num / len(numbers)


print(result)