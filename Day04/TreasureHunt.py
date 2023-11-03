line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter the pos: ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

pos1 = position[0]
pos2 = position[1]

# print(pos1)


# ...

if pos1 == "A":
    pos1 = 0
elif pos1 == "B":
    pos1 = 1
else:
    pos1 = 2

if pos2 == "1":
    line1[pos1] = " X "
elif pos2 == "2":
    line2[pos1] = " X "
else:
    line3[pos1] = " X "

print(f"{line1}\n{line2}\n{line3}")