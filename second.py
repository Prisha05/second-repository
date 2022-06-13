first=input('enter first number:')
operator=input("emter operator (+,-,*,/,%):")
second=input("enter second number:")

if operator == "+":
    print(first+second)
elif operator == "-":
        print(first -second)
elif operator == "*":
    print(first*second)
elif  operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid Operation")