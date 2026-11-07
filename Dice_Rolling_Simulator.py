print("welcome to Dice Rolling Simulator")
i=1
print("(1)To roll the dice")
print("(2)To roll two dices")
print("(3)Exit")
while i<=6:
    a=int(input("Enter your choice in number:"))
    if a==1:
        import random
        i=random.randint(1,6)
        print("After one dice roll",i)
    elif a==2:
        import random
        i=random.randint(1,6)
        import random
        b=random.randint(1,6)
        print(f"After two dices roll:{i},{b}")
        print("Total of two dices roll:",i+b)
    elif a==3:
        print("Thank you")
        break
    else:
        print("Invalid Choice,try again")