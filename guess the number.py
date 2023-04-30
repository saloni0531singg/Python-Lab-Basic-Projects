import random
att=3
n=random.randint(1,100)
a=input("  Welcome to Number Game  ")
while att:
    u_guess=int(input("Guess The Number"))
    if u_guess<n:
        print("too small")
        print("attempt left",att-1)
    elif u_guess>n:
        print("too big")
        print("attempt left",att-1)
    else:
        print("congratulations ,You win")
    att-=1
print("game over,the number is",n)
