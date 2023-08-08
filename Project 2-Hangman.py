#-------------------------------------------------------------------------------
# Name:        Hangman
# Purpose:
#
# Author:      Devansh Rajput
#
# Created:     19-09-2022
# Copyright:   (c) Devansh Rajput 2022
# Licence:     <Devansh Rajput licence>
#-------------------------------------------------------------------------------

import random
def hangman():

    word = random.choice(["airplane" , "boat" , "baby" , "ear" , "scissor" , "cough" , "phone" , "laugh" , "hairbrush" , "sneeze" , "hammer" , "book" , "phone" , "toothbrush" , "archer" , "ghost" , "balloon" , "football" , "soccer" , "volleyball" , "elephant" , "giraffe" , "monster" , "birthday" , "president" , "apartment" , "waterfall" , "window" , "flashlight" , "archery" , "basketball" , "hockey" , "table tennis" , "whale" , "snake" , "elephant" , "kangaroo" , "shark" , "caterpillar" , "cockroach" , "monkey" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 5
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 4:
                print("4 turns left")
                print("------------")
                print("   __O__    ")
                print("     |      ")
                print("    / \     ")
                print("------------")
            if turns == 3:
                print("3 turns left")
                print("------------")
                print("    _O_     ")
                print("   / | \    ")
                print("    / \     ")
                print("------------")
            if turns == 2:
                print("2 turns left")
                print("------------")
                print("     0      ")
                print("    /|\     ")
                print("    / \     ")
                print("------------")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting,Take care!")
                print("------------")
                print("     O_    ")
                print("    /|\     ")
                print("    / \     ")
                print("------------")
            if turns == 0:
                print("You lose!")
                print("You let a kind man die")
                print("------------")
                print("     O_|   ")
                print("    /|\     ")
                print("    / \     ")
                print("------------")
                break


name = input("Enter your name")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 5 attempts")
hangman()
print()