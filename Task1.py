#Taking the input from the user

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

#Performing the operation

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2

if num2!=0:
    division=num1 / num2
else:
    divison=" Undefined"

#Display the output

print("Addition: ",addition)        
print("Subtraction: ",subtraction)
print("Multiplication: ",multiplication)
print("Division: ",division)