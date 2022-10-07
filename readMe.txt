#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:58:11 2021

@author: charleesiu
"""
*******************************************
Name: Charlie Liu
Date: Ocotober 9
File: readme.txt

This file explains:
    - how my program works 
    - anyone I described my work with 
    - why I made the design decisions I did
*******************************************

HOW MY PROGRAM WORKS:

1. game.py

The function main()is a one-time-use, special, specific function which compiles 
the functions the program needs. 
    - It welcomes the user, starts the game, runs the game, and 
      says goodbye to the user once finished
   

The function play_game() plays one interactive game of bulls and cows with the user
    - It gives the context of the game, assigns the secret number to answer, 
      and assigns the user's input to guess
    - It also prints the bulls and cows score after each guess, and counts 
      the number of guesses it takes to get the right answer

2. bulls_and_cows.py

The function generate_secret() creates the string of 4 unique digits from 0 to 9
that acts as the secret answer in the game
    - It generates a random sample of 4 unique digits as a list, then adds each
      element of the list together into one coherant string 
      
      
The function how_many_bulls returns how many bulls as an integer value
that the user scores given the answer and their guess
    - It parses through the two strings, answer and guess, and compares the
      value and position of each element in guess to each element in answer
    - If the value and position match, bulls increases by 1
 
 
The function how_many_cows returns how many cows as an integer value that the 
user scores given the answer and their guess
    - It parses through answer and guess, and compares the value and position 
      of each element in answer to each element in guess
    - The comparison direction is reversed since answer's digits are always 
      unique, solving a problem of the possibility of the user guessing 
      repeated digits
    - If the value of the element in answer is in guess, but the position does
      NOT match, cows increases by 1

PEOPLE I DISCUSSED MY WORK WITH:
    - Professor Canon (Office Hours)

DESIGN DECISIONS:
    - I used .sample() in generate_secret because it's a built in Python function
      that generates a list of unique digits with 0 being a possible first element
      
    - I initially wrote a line of code in how_many_bulls() to check each separate
      element in the strings, but then I amde it more efficient by setting up
      a for-loop 
      
    - I got stuck at how_many_cows() because when comparing guess to answer, the 
      problem of possible repeated digits came up. By comparing answer to guess
      instead, that problem was solved and the count of cows was correct
      
      