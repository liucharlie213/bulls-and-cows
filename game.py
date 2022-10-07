#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:06:57 2021

@author: charlesliu
"""

# *******************************************
# Name: Charlie Liu CRL2157
# Date: Ocotober 9
# File: game.py

# This program plays the game bulls and cows with the user
# *******************************************


import bulls_and_cows as bc

def main():
    #Please do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again = 'y'
    
    while(again == 'y'):
        play_game()
        again = input('Would you like to play again (y/n) ')
   
    print('So long sucker!')
    
def play_game():
    '''Plays one interative game of bulls and cows on the console'''
    
    print("I'm thinking of a secret number made of 4 digits with no repeats")    
    
    answer = bc.generate_secret()
    # This is the secret answer!
    guess = input("What number do you think it is? ")
    # This is the user's guess!
    
    guess_counter = 1
    # Counts the number of guesses it takes the user to guess the secret answer
    
    while bc.how_many_bulls(guess, answer) != 4:
    # Once bulls = 4, the user has guessed the secret number and the game is over
    # Runs until bulls = 4
    
        print("Bulls: {}".format(bc.how_many_bulls(guess, answer)))
        print("Cows: {}".format(bc.how_many_cows(guess, answer)))  
        print("Keep Guessing!")
        # Print the number of bulls and cows the user scored with their latest guess
        
        guess = input("What number do you think it is? ")
        # This is the users next guess (since bulls is not yet 4)
        # Reassigns the variable guess with a new string
        
        guess_counter += 1
        # Since the game hasn't ended, add 1 to the guess count every new guess
    
    print("You got it! The secret number was: {}".format(answer))
    print("Bulls: {}".format(bc.how_many_bulls(guess, answer)))
    print("Cows: {}".format(bc.how_many_cows(guess, answer)))
    print("It only took you {} tries!".format(guess_counter))
                                   
main()