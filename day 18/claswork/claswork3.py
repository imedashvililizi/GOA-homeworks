"""შექმენით პროგრამა სადაც გექნებათ ორი სია. პირველ სიაში 10-იდან 20-ის ჩათვლით ლუწი რიცხვები, ხოლო მეორეში კენტები დაამატეთ. საბოლოოდ გამოიტანეთ ეს სიები 
"""

odd_list = []
even_list = []

for i in range(10, 21):
    if i %2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
print(odd_list)
print(even_list)