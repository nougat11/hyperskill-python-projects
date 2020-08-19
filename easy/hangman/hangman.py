from random import choice
from string import ascii_lowercase

def game():
    words_list = ("python", "java", "kotlin", "javascript")
    right_word = choice(words_list)
    mask_word = '-' * len(right_word)
    tries = 8
    win = False
    bucket = []
    while tries > 0:
        print()
        print(mask_word)
        letter = input("Input a letter: > \n")
        if (len(letter) != 1):
            print("You should input a single letter")
        elif (letter not in ascii_lowercase):
            print("It is not an ASCII lowercase letter")
        elif (letter in bucket):
            print('You already typed this letter')
        else:
            bucket.append(letter)
            if letter in right_word:
                for i in range(len(right_word)):
                    if letter == right_word[i]:
                        mask_word = mask_word[:i] + letter + mask_word[i+1:]
                if (mask_word == right_word):
                    tries = 0
                    win = True
            else:
                print("No such letter in the word")
                tries -= 1
    if win:
        print()
        print(right_word)
        print('You guess the word!')
        print('You survived!')
    else:
        print("You are hanged!")


   
print("H A N G M A N")
while True:
    action = input('Type "play" to play the game, "exit" to quit: > ')
    if (action == 'play'):
        game()
    if (action == 'exit'):
        break
