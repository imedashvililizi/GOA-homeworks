"""სიაში შეიტანეთ 30-იდან 50-ის ჩათვლით არსებული ყველა რიცხვი.
 შემდეგ დაითვალეთ ამ სიაში არსებული კენტი რიცხვები და დაბეჭდეთ მათი რაოდენობა.
"""


list = []
for i in range(30,50 + 1):
    list.append(i)
    
    if i % 2 != 0:
         print()
print(len(list))