def output(water, milk, beans, cups, money):
    print()
    print('The coffe machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disaposable cups')
    print(money, 'of money')
    print()

water, milk, beans, cups, money = 400, 540, 120, 9, 550
coffee_machine = True
while coffee_machine:
    action = input('Write action (buy, fill, take, remaining, exit): \n')
    if (action == "take"):
        print(f'I gave you ${money}')
        money = 0
        print()
    if (action == 'buy'):
        print()
        type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if (type == "1"):
            if water >= 250 and beans >= 16 and cups >= 1:
                water, beans, cups, money = water - 250, beans - 16, cups - 1, money + 4
                print('I have enough resources, making you a coffee!')
            else:
                print("Not enough resources")
        if (type == "2"):
            if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
                water, milk, beans, cups, money = water - 350, milk - 75, beans - 20, cups - 1, money + 7
                print('I have enough resources, making you a coffee!')
            else:
                print("Not enough resources")
        if (type == "3"):
            if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
                water, milk, beans, cups, money = water - 200, milk - 100, beans - 12, cups - 1, money + 6
                print('I have enough resources, making you a coffee!')
            else:
                print("Not enough resources")
        print()
    if (action == 'fill'):
        water += int(input("Write how many ml of water do you want to add:\n"))
        milk += int(input("Write how many ml of milk do you want to add:\n"))
        beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    if (action == 'remaining'):
        output(water, milk, beans, cups, money)
    if (action == 'exit'):
        coffee_machine = False


