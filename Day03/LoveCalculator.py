name1 = input("Enter the name1: ").upper()
name2 = input("Enter the name2: ").upper()

name = name1+name2

count1 = 0
count2 = 0

for i in name:
    if(i in 'TRUE'):
        count1 = count1 + 1
    if(i in 'LOVE'):
        count2 = count2 + 1

count1 = count1 * 10
count = count1 + count2

if(count > 90 or count < 10):
    print(f"Your score is {count}, you go together like coke and mentos.")
elif(count > 40 and count < 50):
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")