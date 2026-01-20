num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

addition=num1+num2
print(f"addition:{num1}+{num2}={addition}")

subraction=num1-num2
print(f"subraction:{num1}-{num2}={subraction}")

multiplication=num1*num2
print(f"multiplication:{num1}*{num2}={multiplication}")

if num2!=0:
   division=num1/num2
   print(f"division:{num1}/{num2}={division}")
else:
   print("division:Error! cannot divide by zero.")
