"""სიაში შეიტანეთ თქვენთვის სასურველი 10 რიცხვი. დაბეჭდეთ ამ სიაში არსებული ყველაზე დიდი რიცხვი, 
მინიშნება: გამოიყენეთ for ციკლი. არ გამოიყენოთ max მეთოდი.
"""
list = [1,4,9,15,17,3,10,23,48,5]

max = list[0]

for i in list:
    if i > max:
        max = i

print(max)