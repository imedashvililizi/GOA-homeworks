def fake_bin(x):
    result = ""
    
    for char in x:
        if int(char) < 5:
            result = result + "0"
        else:
            result = result + "1"
    
    return result