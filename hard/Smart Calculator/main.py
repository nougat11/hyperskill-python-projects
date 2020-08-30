from string import ascii_letters,digits
from sys import exit
stack = {}
def help():
    print("The program calculates the sum and sub of numbers")

def isdigit(number):
    try:
        k = int(number)
    except ValueError:
        return False
    else:
        return True
def calculation(z):
    array = []
    k = 0
    for i in z:
        if isdigit(i):
            array.append(int(i))
        else:
            a2 = array.pop()
            a1 = array.pop()
            if i == '+':
                k = a1 + a2
            if i == '-':
                k = a1 - a2
            if i == '*':
                k = a1 * a2
            if i == '/' and a2 != 0:
                k = a1 // a2
            if i == '^':
                k = a1 ** a2
            array.append(k)
    return array[0]




def correct(z):
    for i in z:
        if i not in ascii_letters:
            return False
    return True


def assigment(z):
    if len(z.split()) > 4:
        print("Invalid assigment")
        return
    left, right = z[:z.find('=')].strip(), z[z.find('=')+1:].strip()
    if not isdigit(right):
        if correct(left):
            if correct(right):
                if right in stack.keys():
                    stack[left] = stack[right]
                else:
                    print("Unknown variable")
            else:
                print("Invalid assigment")
        else:
            print("Invalid identifier")
    else:
        if correct(left):
            stack[left] = int(right)
        else:
            print("Invalid identifier")


def command(z):
    if z == "/exit":
        print("Bye")
        exit(0)
    if z == "/help":
        help()
    else:
        print("Unknown command")

def show(z):
    if z in stack.keys():
        print(stack[z])
    else:
        print("Unknown variable")


def check_group(c):
    groups = (ascii_letters + digits, "+", "-", "*", "/", "^", " ", "(", ")")
    z = c[1] if len(c) > 1 else c[0]
    for i in groups:
        if z in i:
            return groups.index(i)

def parser(z):
    array = []
    now_group = -5
    sub = ""
    for symbol in z:
        group = check_group(symbol)
        if group in (2, 1) and now_group in (-5, 7):
            group = 0
        if group == now_group and group not in (7, 8):
            sub += symbol
        else:
            array.append(sub)
            sub = symbol
            now_group = group
    array.append(sub)
    return array

def filter(z):
    array = []
    for i in z:
        if i.count(" ") > 0 or i == "":
            continue
        elif i.count('+') == len(i):
            array.append('+')
        elif i.count('-') == len(i):
            array.append('-' if len(i) % 2 else '+')
        else:
            array.append(i)
    return array


def check_error(z):
    for i in range(len(z)):
        group = check_group(z[i])
        if group != 0 and z[i] not in ('(', ')', '*', '-', '^', '+', '/'):
            print("Invalid expression")
            return True
        else:
            if all(map(lambda c: c in ascii_letters, z[i])):
                z[i] = stack[z[i]]
    bracket = []
    for i in z:
        if i == '(':
            bracket.append(1)
        if i == ')':
            if len(bracket) < 1:
                print("Invalid expression")
                return True
            else:
                bracket.pop()
    if len(bracket) > 0:
        print("Invalid expression")
        return True
    return False
def rank(n):
    if n in ('(', ')'):
        return 0
    if n in ('+', '-'):
        return 1
    if n in ('*', '/'):
        return 2
    if n == '^':
        return 3

def postfix(z):
    array = []
    substack = []
    for i in z:

        if isdigit(i):
            array.append(i)
        else:

            if len(substack) == 0:
                substack.append(i)
            elif i == '(':
                substack.append(i)
            elif i == ')':
                while substack[-1] != '(':
                    array.append(substack.pop())
                substack.pop()
            else:

                if len(substack) > 0:

                    while rank(substack[-1]) >= rank(i):
                        array.append(substack.pop())
                        if len(substack) == 0:
                            break
                substack.append(i)
    while len(substack) > 0:
        array.append(substack.pop())

    return array












if __name__ == "__main__":
    while True:
        z = input()
        if z == "":
            continue
        if z.count('=') > 0:
            assigment(z)
        elif z[0] == '/':
            command(z)
        else:
            if len(z.split()) == 1:
                show(z)
            else:
                z = parser(z)
                z = filter(z)
                if check_error(z):
                    continue
                d = postfix(z)
                print(calculation(d))
            #if len(z) == 1 and not isdigit(z[0]):
            #    show(z[0])
            #else:
            #    result, flag = calculation(z)
            #    if flag:
            #        print(result)
