"""უარყოფითი რიცხვების ამოღება: დაწერეთ ალგორითმი, 
რომელიც მიიღებს მთელ რიცხვთა სიას და ამოიღებს ყველა უარყოფით რიცხვს, დაბეჭდავს ახალ სიას ამ ელემენტების გარეშე."""

numbers = []

for i in range(7):
    num =int(input("enter number :"))
    if num > 0:
            numbers.append(num)

print(numbers)
