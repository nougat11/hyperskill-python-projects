from random import choice
print("H A N G M A N")
word = input("Guess the word: > ")
words_list = ("python", "java", "kotlin", "javascript")
right_word = choice(words_list)
if (word == right_word):
    print("You survived!")
else:
    print("You are hanged!")
