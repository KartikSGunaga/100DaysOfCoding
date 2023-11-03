size = input("Which size: ").upper()
pep = input("Add pepperoni: ").upper()
cheese = input("Add cheese: ").upper()

if(cheese == "Y"):
    total = 1
else:
    total = 0

if(size == "L"):
    total = total + 25
    if(pep == "Y"):
        total = total + 3
elif(size == "M"):
    total = total + 20
    if(pep == "Y"):
        total = total + 3
else:
    total = total + 15
    if(pep == "Y"):
        total = total + 2 

print(f"""Thank you for choosing Python Pizza Deliveries!
Your final bill is: ${total}.""")