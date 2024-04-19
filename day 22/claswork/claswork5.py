def odd(numbers):
    num = 0
    for i in numbers:
        if numbers % 2 != 0:
            num += i
    return num
print(odd([2,3,6,9,12,15])+ 5)