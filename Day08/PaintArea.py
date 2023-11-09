height = int(input("enter the height: "))
width = int(input("enter the width: "))

def paintArea(height, width):
    return(height * width)

print(f"the number of cans required is: {paintArea(height, width)}")