from math import log, ceil, trunc
import sys

args, type_, payment, principal, interest, periods = sys.argv, " ", 0, 0, 0, 0
for arg in args:
    if arg.startswith("--type"):
        type_ = arg[7:]
    if arg.startswith("--payment"):
        payment = int(arg[10:])
    if arg.startswith("--principal"):
        principal = int(arg[12:])
    if arg.startswith("--interest"):
        interest = float(arg[11:])
    if arg.startswith("--periods"):
        periods = int(arg[10:])
if type_ == "diff":
    if payment != 0 or principal == 0 or periods == 0 or interest == 0:
        print("Incorrect parameters")
    else:
        deposits = []
        for j in range(1, periods + 1):
            i = interest / 12 / 100
            money = ceil(
                principal / periods + i * (principal - (principal * (j - 1) / periods))
            )
            deposits.append(money)
            print(f"Month {j}: paid out {money}")
        print()
        print("Overpayment =", sum(deposits) - principal)
if type_ == "annuity":
    if all([principal, periods, interest]):
        i = interest / 12 / 100
        a = ceil(principal * ((i * (i + 1) ** periods) / ((i + 1) ** periods - 1)))
        print("Your annuity payment =", a)
        print("Overpayment =", a * periods - principal)
    elif all([payment, periods, interest]):
        i = interest / 12 / 100
        a = trunc(payment / (i * (i + 1) ** periods / ((i + 1) ** periods - 1)))
        print(f"Your credit payment = {a}!",)
        print("Overpayment =", payment * periods - a)
    elif all([payment, principal, interest]):
        i = interest / 12 / 100
        n = ceil(log(payment / (payment - i * principal), i + 1))
        print(f"You need {n} months to repay this credit!")
        print(f"Overpayment = {n * payment - principal}")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
