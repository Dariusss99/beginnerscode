import random

print("Hey, nice to see you! What's your name? ")
name = input()
print("How much money you got? ")
balance = round(float(input()))

while True:
    if balance <= 0:
        print("You lost everything")
        break
    else:
        print(f"Your current balance is: {round(balance)}. \n")
        print(f"Ok {name}, How much money are you betting? ")
        while True:
            money = round(float(input()))
            if money > balance:
                print("You don't have that amount of money. Try a different amount")
            elif 0 < money <= 100:
                print("I like that amount. \n"
                    "Let's start. ")
                break
            elif money > 100:
                print("Sorry the max bet is 100. \n"
                    "try a different amount. ")
            else:
                print("you gotta bet something. \n"
                    "So how much? ")

        player_hand = random.randint(1, 14)
        while True:
            print(f"Your hand is: {player_hand}")
            if player_hand > 21:
                balance -= money
                print("Sorry you got too much. You lost. ")
                break
            elif player_hand == 21:
                print("You have 21")
                break
            else:
                print("Hit or Stand? ")
                player_choise = input()
                if player_choise == "Hit" or player_choise == "hit" or player_choise == "h":
                    player_hand += random.randint(1, 14)
                elif player_choise == "Stand" or player_choise == "stand" or player_choise == "s":
                    break

        if player_hand <= 21:
            dealer_hand = random.randint(1, 14)
            while True:
                if dealer_hand > 21:
                    print(f"The dealer lost \n"
                        f"He got: {dealer_hand}")
                    balance += money
                    break
                elif 16 <= dealer_hand <= 21:
                    print(f"The dealer has: {dealer_hand}")
                    break
                else:
                    dealer_hand = dealer_hand + random.randint(1,14)

        if player_hand <= 21 and dealer_hand <= 21:
            if player_hand == dealer_hand:
                print("you got even \n")

            elif dealer_hand < player_hand <= 21:
                balance += money
                print(f"you won! \n")

            elif player_hand < dealer_hand <= 21:
                balance -= money
                print(f"you lost! \n")
        else:
            continue



print("Hope to see you soon!")











