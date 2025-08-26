# Slot machine

"""
Slot machine like in casino, when user make a deposit and spin the game, the output has 3 rows and 3 columns
Before spinning, user can decide de bet on one line, 2 lines or 3. More the lines is, more the bet is
less the winning is
"""

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
ROWS = 3
COLS = 3 # rows and columns of the slot machine



def check_winnings(columns,lines, bet, values):
    winnings = 0
    winnings_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_line.append(line +1)

    return winnings, winnings_line


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count_slot in symbols.items():
        for _ in range(symbol_count_slot):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns



def print_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end= " | ")
            else:
                print(column[row],end="")
        print()




def deposit():
    while True:
        balance = input("Enter the amount of your deposit :")

        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break

            else:
                print("Deposit needs to be greater than $ 0.00")

        else:
            print("Invalid Entry")

    return balance

def get_lines():
    while True:
        lines = input("Enter the number of lines to bet on :")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break

            else:
                print("Line must be between 1 and 3")

        else:
            print("Invalid Entry, type error ")

    return lines


def make_bet():
    while True:
        bet = input("Enter the amount to bet on the lines selected :")

        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break

            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")

        else:
            print("Invalid Entry")

    return bet

def spin(balance):
    lines = get_lines()
    while True:
        bet = make_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance, you have {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winnings_line = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}")
    print(f"You won on: ", *winnings_line)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is : ${balance}")
        print("*************************")
        print("*******SLOT MACHINE******")
        print("*************************")

        choice = input("Press any key to play (q to quit:) ")
        if choice == 'q':
            break
        else:
             balance += spin(balance)

    print(f"You've left with {balance}")

main()




