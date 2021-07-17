import time
import turtle
import random
from dinnerList import proteinList, veggieList, carbsList
from colorama import Fore, Style
from deep_translator import GoogleTranslator
screen = turtle.Screen()
sheldon = turtle.Turtle()
screen.bgcolor("black")
sheldon.shape("circle")
sheldon.color("white")
sheldon.speed(10)
sheldon.hideturtle()

new_success = None

x = random.randrange(1,10)

import bloodmoon
def runTheGoddamnGame():
    """While writing the program, I encountered a very strange issue - directly importing bloodmoon.py into __main__.py
    caused a crippling error, so I'm using this jank af workaround."""
    bloodmoon.runGame()

