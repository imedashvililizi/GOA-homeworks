"""დავალება: შექმენით პროგრამაც, სადაც გექნებათ ორი სია. პირველში 1-იდან 10-ის ჩათვლით დაამატეთ ლუწი რიცხვები, ხოლო მეორეში კენტები. 
გამოიყენეთ for ციკლი და append ფუნქცია"""
even_numbers = []
odd_numbers = []

for i in range(1,10 + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(even_numbers)
print(odd_numbers)