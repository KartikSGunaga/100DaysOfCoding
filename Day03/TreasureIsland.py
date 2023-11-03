print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

move1 = input("left or right?: ").lower()
if(move1 != "left"):
    print("""Fall into a hole.
Game Over.""")
else:
    move2 = input("swim or wait: ").lower()
    if(move2 != "wait"):
        print("""Attacked by trout.
Game Over.""")
    else:
        move3 = input("Which door?: ").lower()
        if(move3 == "yellow"):
            print("You win!")
        elif(move3 == "blue"):
            print("""Eaten by beasts.
Game Over.""")
        elif(move3 == "red"):
            print("""Burned by fire.
Game Over""")
        else:
            print("Game Over.")