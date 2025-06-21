import random

def spin():
# spinnig mechanism

    symbols = ['🍒', '🍉', '🍋', '🔔']

    result = []

    for i in range(3):
        result.append(random.choice(symbols))

    return result

def print_row(row):

    print(" ".join(row))

def get_payout(row, bet):
# assigning/winning mechanism

    if row[0] == row[1] == row [2]:
        symbol = row[0]
        if symbol == '🍒':
            print(f"You won: ")
            return bet * 3
        elif symbol == '🍉':
            print(f"You won: ")
            return bet * 5
        elif symbol == '🍋':
            print(f"You won: ")
            return bet * 7
        elif symbol == '🔔':
            print(f"You won: ")
            return bet * 10
    return 0

def main():
    balance = 100
# main code
    while True:

        print("*************************")
        print("Welcome to Python Slots ")
        print("Symbols: 🍒 🍉 🍋 🔔")
        print("*************************")


        bet_input = input("Enter your bet amount: ")


        if not bet_input.isdigit():
            print("Please enter a number")


        bet = int(bet_input)



        row = spin()
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"You won {payout}")
        else:
            print("You lost")

        u_exit = input("To exit press: 1 else press Enter.")
        if u_exit == "1":
            break

        if bet > balance:
            print("Insufficient balance.")
        elif bet <= 0:
            print("Bet must be greater than 0. ")
        else:
            continue
    balance -= bet
    print(balance)


if __name__ == '__main__':
    main()