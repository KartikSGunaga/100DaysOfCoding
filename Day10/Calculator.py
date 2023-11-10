response = 1
ans = 0
count = 0

def add(n1 , n2):
    """Addition of n1 and n2"""
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

while(response == 1):
    if(count == 0):
        n1 = float(input("Enter the first number: "))
    else:
        answer = input("Press + to retain the answer, - to start fresh: ")
        if(answer == '+'):
            n1 = ans
        else:
            n1 = float(input("Enter the first number: "))

    operation = input("Enter the operation (add, sub, multiple, divide): ").lower()
    n2 = float(input("Enter the second number: "))

    match operation:
        case "add":
            ans = add(n1, n2)
            print(f"The sum is: {add(n1, n2)}") 
        case "sub":
            ans = sub(n1, n2)
            print(f"The difference is: {sub(n1, n2)}")
        case "multiply":
            ans = multiply(n1, n2)
            print(f"The product is: {multiply(n1 , n2)}")
        case "divide":
            ans = divide(n1, n2)
            print(f"The dividend is: {divide(n1, n2)}")

    response = int(input("Press 1 to continue, 0 to terminate."))
    count += 1
        
        

