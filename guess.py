#!/usr/bin/env python

from random import randint

def guess():
    times = 3
    age = randint(18, 30)
    while(times):
        try:
            ans = int(input("Guess my age(18-30):"))
        except ValueError as e:
            print("Warning:", e)
        else:
            if ans == age:
                print("Congratulations, you guessed it!")
                break
            else:
                pr = "Sorry, it should be bigger!" if ans < age \
                        else "Sorry, it should be smaller!"
                print(pr)
                times -= 1
    if not times:
        print("Game over!", "\nMy age is:", age, "\n")
    try:
        ch = input("Again?(y/n)").strip()[0].lower()
    except IndexError:
        pass
    else:
        if ch in "yn":
            if ch == "y":
                print()
            else:
                exit()
        else:
            print("Continue the game!")
            print("Press Ctrl+c to quit!\n")

if __name__ == "__main__":
    while True:
        guess()

