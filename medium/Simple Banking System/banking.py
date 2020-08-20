import random
import sys
import sqlite3


def generate_can():
    number = "1"
    while len(number) != 9:
        number = random.randint(0, 999999999)
        while number in BankingSystem.accounts:
            number = random.randint(0, 999999999)
        number = str(number)
        number = '0' * (9 - len(number)) + number
    return number


class BankingSystem:
    accounts = []

    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")



    def create_account(self):

        INN = "400000"
        account_identifier = generate_can()
        checksum = BankingSystem.lunh_algorithm(INN + account_identifier)
        PIN = BankingSystem.generate_pin()
        card_number = INN + account_identifier + checksum
        self.cur.execute(f"INSERT INTO card (id, number, pin) VALUES ({int(account_identifier)}, {card_number}, {PIN})")
        self.conn.commit()
        BankingSystem.accounts.append( {
            "PIN": PIN,
            "balance": 0,
            "number": card_number
        })
        return card_number, PIN



    @staticmethod
    def generate_pin():
        PIN = ""
        for i in range(4):
            PIN += str(random.randint(0, 9))
        return PIN

    @staticmethod
    def login(card_number, PIN):
        for user in BankingSystem.accounts:
            if user["PIN"] == PIN and user["number"] == card_number:
                return user
        return None

    @staticmethod
    def lunh_algorithm(string):
        card = [int(i) for i in string]
        for i in range(15):
            if i % 2 == 0:
                card[i] *= 2
            if card[i] > 9:
                card[i] -= 9
        return str((10 - sum(card) % 10) % 10)


bank = BankingSystem()
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    action = int(input())
    if action == 1:
        print()
        card_number, pin = bank.create_account()
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print('Your card PIN:')
        print(pin)
        print()
    if action == 2:
        print()
        credit_number = input("Enter your card number:\n")
        PIN = input("Enter your PIN:\n")
        user = BankingSystem.login(credit_number, PIN)
        if user is None:
            print("Wrong card number or PIN!")
            print()
        else:
            print("You have successfully logged in!")
            while True:
                print()
                print("1. Balance")
                print("2. Add income")
                print("3. Do transfer")
                print("4. Close account")
                print("5. Log out")
                print("0. Exit")
                subaction = input('>')
                if subaction == "1":
                    bank.cur.execute(f"SELECT balance FROM card WHERE number = {credit_number}")
                    print(bank.cur.fetchone()[0])
                if subaction == "2":
                    print()
                    bank.cur.execute(f"SELECT balance FROM card WHERE number = {credit_number}")
                    bank.conn.commit()
                    balance = bank.cur.fetchone()[0]
                    n = int(input("Enter income?\n"))
                    print("Income was added!")
                    balance += n
                    bank.cur.execute(f"UPDATE card SET balance = {balance} WHERE number == {credit_number}")
                    bank.conn.commit()
                if subaction == "3":
                    print()
                    print("Transfer")
                    number = input("Enter card number:\n")
                    if (number == credit_number):
                        print("You can't transfer money to the same account!")
                        continue
                    if (bank.lunh_algorithm(number[:15]) != number[15]):
                        print("Probably you made mistake in the card number. Please try again!")
                        continue
                    bank.cur.execute(f"SELECT true FROM card WHERE number = {number};")
                    if bank.cur.fetchone() is None:
                        print("Such a card does not exist.")
                        continue
                    money = int(input("Enter how much money you want to transfer:\n"))
                    bank.cur.execute(f"SELECT balance FROM card WHERE number = {credit_number}")
                    balance = bank.cur.fetchone()[0]
                    if (balance < money):
                        print("Not enough money!")
                    else:
                        bank.cur.execute(f"UPDATE card SET balance = {balance - money} WHERE number == {credit_number}")
                        bank.conn.commit()
                        bank.cur.execute(f"SELECT balance FROM card WHERE number = {number}")
                        bal = bank.cur.fetchone()[0]
                        bank.cur.execute(f"UPDATE card SET balance = {bal + money} WHERE number == {number}")
                        bank.conn.commit()
                if subaction == '4':
                    print("The account has been closed!")
                    bank.cur.execute(f"DELETE FROM card WHERE number = {credit_number}")
                    bank.conn.commit()
                    break
                if subaction == '5':
                    break
                if subaction == '0':
                    sys.exit(0)
    if action == 0:
        break

