"""შექმენით პროგრამა, სადაც მოხმარებელს შეეკითხებით ხუთ რიცხვს. ლუწები ერთ სიაში, ხოლო კენტები მეორეში დაამატეთ
დავალება"""
even_nums=[]

odd_nums=[]

for i in range(5):
    user_nums=int(input("enter enter number"))

    if i%2 == 0:
        even_nums.append(user_nums)
    else:
        odd_nums.append(user_nums)
print(even_nums)
print(odd_nums)