correct_password=2911
attempt=0
while attempt <3:
    pin=int(input("Enter a password:"))
    if pin== correct_password:
     print("Login Successfully")
     break
    else:
        attempt=attempt+1
        print("Wrong password")
    if attempt==3:
        print("Accound Locked")
