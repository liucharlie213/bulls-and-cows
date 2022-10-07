#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:08:12 2021

@author: charlesliu
"""

# *******************************************
# Name: Charlie Liu CRL2157
# Date: Ocotober 9
# File: bulls_and_cows.py

# This file creates three functions which generate and return a secret answer 
# for the bulls and cows game, and returns the score of bulls and cows after
# each guess
# *******************************************

import random

def generate_secret():
    '''Generate a 4 digit number with no repeat digits''
    It converts the number to a string and returns it'''
    
    s_list = random.sample(range(10),4)
    # Built-in function .sample() 
    # To generate a random list of 4 unique digits from 0-9 
    
    secret = ""
    # Initializes to empty string so it can be referred to in the for-loop
    
    for digit in s_list:
        secret += str(digit)
    # Adds each string element together to form one string of 4 unique digits
    
    return secret

def how_many_bulls(guess, answer):
    '''Return the number of bulls as an int that the guess earns when the 
    secret number is answer. Both answer and guess should be string'''
 
    bulls = 0
    # Bulls will be changed in the for-loop
    
    for i in range(4):
        if answer[i] == guess[i]:
            bulls += 1
    # If the position and value of each element is the same, bulls increases by 1
    
    return bulls

def how_many_cows(guess, answer):
    '''Returns the number of cows as an int that the guess earns when the
    secret number is answer. Both answer and guess should be string'''
   
    cows = 0
    # Cows will be changed in the for-loop
    
    for i in range(4): 
        if answer[i] in guess and answer[i] != guess[i]:
            cows += 1
    # Checks the elements in answer against guess, since answer can't have repeats
    # Solves the problem of the user possibly guessing repeated digits
    # If each element in answer is in guess AND the indexes do not match, cows increases by 1
    
    return cows

