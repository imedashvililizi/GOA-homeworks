registered_password = "lizi12345"

authorized = False

while authorized != True:
    user_input = (input("enter your password"))

    if user_input == registered_password:
        print("accses granted")
        autoraized = True
    else:
        print("incorrect please try again")

print("weel done")