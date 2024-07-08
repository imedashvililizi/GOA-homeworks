def show_sequence(n):
    if n < 0 :
        return str(n)+"<0"
    elif n == 0:
        return "0=0"
    sum = 0
    string_result = []
    for i in range(n+1):
        sum += i
        string_result.append(str(i))
    return "+".join(string_result)+" = " + str(sum)