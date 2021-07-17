# I know I should've added more comments, but I'm lazy and only now realize how inefficient this code is.
# For the record, I didn't know functions existed when I started this program. yeah.
# module imports
import time # find and replace --> comment out time if you want a faster (but less cool) experience
import turtle
import random
import settings # may not be neccesary, but I'm scared
from dinnerList import proteinList, veggieList, carbsList
from colorama import Fore, Style
from deep_translator import GoogleTranslator
import bloodmoonGateway
from settings import Settings
bm_settings = Settings()

# for some reason this line of code prevents a crash. don't ask me why. i don't know. (╯°□°）╯︵ ┻━┻
stupid_var = bloodmoonGateway.x

# Opening setup

screen = turtle.Screen()
sheldon = turtle.Turtle()
screen.bgcolor("black")
sheldon.shape("circle")
sheldon.color("white")
sheldon.speed(10)
sheldon.hideturtle()

# function declarations

def lowStat(name, amount):
    print(Fore.RED + "Your " + name + " stat is low!" + Style.RESET_ALL)
    time.sleep(0.75)
    print(name + " is currently at " + str(amount) + ".")
    time.sleep(0.75)
    print("If this gets too low, it's very bad!")


def advancement(color, title):
    sheldon.reset()
    sheldon.hideturtle()
    screen.reset()
    screen.resetscreen()
    screen.bgcolor("black")
    sheldon.hideturtle()
    sheldon.speed(5)
    sheldon.pensize(10)
    sheldon.up()
    sheldon.goto(-150, -150)
    sheldon.color(color)
    screen.tracer(10)
    sheldon.down()
    for advancementSquare in range(4):
        sheldon.forward(300)
        sheldon.left(90)
    screen.update()
    sheldon.up()
    sheldon.goto(-100, -30)
    sheldon.pensize(15)
    sheldon.down()
    sheldon.setheading(315)
    sheldon.forward(70)
    sheldon.left(90)
    sheldon.forward(200)
    sheldon.pensize(1)
    sheldon.up()
    sheldon.goto(0, -200)
    sheldon.down()
    screen.update()
    sheldon.write("Advancement Made: " + title, False, align="center", font=("Modern", 35))
    sheldon.up()
    screen.update()
    time.sleep(3)
    screen.clearscreen()
    screen.bgcolor("black")


def smallCircle(x, y, color):
    sheldon.up()
    sheldon.speed(0)
    screen.tracer(10)
    sheldon.color(color)
    sheldon.fillcolor(color)
    sheldon.goto(x, y)
    sheldon.down()
    sheldon.begin_fill()
    for circle in range(120):
        sheldon.forward(1)
        sheldon.left(3)
    sheldon.end_fill()
    screen.update()


def smileCurve(x, y, color):
    sheldon.up()
    sheldon.goto(x, y)
    sheldon.color(color)
    sheldon.down()
    screen.tracer(5)
    sheldon.setheading(180)
    sheldon.pensize(5)
    for curveLeft in range(50):
        sheldon.forward(2)
        sheldon.right(1)
    sheldon.up()
    sheldon.goto(x, y)
    sheldon.setheading(0)
    sheldon.down()
    for curveRight in range(50):
        sheldon.forward(2)
        sheldon.left(1)
    screen.update()
    sheldon.pensize(1)


def loadingScreen(x, y, color):
    screen.tracer(10)
    sheldon.up()
    sheldon.goto(x, y)
    sheldon.down()
    sheldon.color(color)
    for bar in range(abs(x)):
        sheldon.setheading(90)
        sheldon.forward(5)
        sheldon.right(90)
        sheldon.forward(1)
        sheldon.right(90)
        sheldon.forward(5)
        sheldon.left(90)
        sheldon.forward(1)
    time.sleep(1)


def coasterBuilder():
    screen.clearscreen()
    screen.bgcolor("light green")
    screen.tracer(10)
    sheldon.hideturtle()
    sheldon.goto(-300, -150)
    sheldon.color("dark grey")
    sheldon.setheading(15)
    sheldon.pensize(10)
    sheldon.speed(1)
    sheldon.forward(20)
    sheldon.left(5)
    sheldon.forward(20)
    sheldon.left(7)
    sheldon.forward(25)
    sheldon.left(9)
    sheldon.forward(25)
    sheldon.left(10)
    sheldon.forward(30)
    sheldon.left(10)
    sheldon.forward(50)
    sheldon.left(10)
    sheldon.forward(70)
    for topCurve in range(28):
        sheldon.right(5)
        sheldon.forward(10)
    sheldon.forward(40)
    sheldon.left(15)
    sheldon.forward(10)
    for unCurve in range(10):
        sheldon.left(5)
        sheldon.forward(10)
    screen.tracer(n=None)
    sheldon.left(7)
    sheldon.forward(50)
    sheldon.left(1)
    sheldon.forward(75)
    screen.update()


def coaster():
    screen.tracer(n=None)
    sheldon.shape("turtle")
    sheldon.up()
    sheldon.speed(1)
    sheldon.goto(-300, -130)
    sheldon.showturtle()
    sheldon.stamp()
    screen.update()
    time.sleep(2)
    screen.update()
    sheldon.setheading(15)
    sheldon.pensize(10)
    screen.update()
    sheldon.speed(1)
    sheldon.showturtle()
    sheldon.forward(20)
    sheldon.stamp()
    screen.update()
    sheldon.left(5)
    sheldon.forward(20)
    sheldon.stamp()
    screen.update()
    sheldon.left(7)
    sheldon.forward(25)
    sheldon.stamp()
    screen.update()
    sheldon.left(9)
    sheldon.forward(25)
    sheldon.stamp()
    screen.update()
    sheldon.left(10)
    sheldon.forward(30)
    sheldon.stamp()
    screen.update()
    sheldon.left(10)
    sheldon.forward(50)
    sheldon.stamp()
    screen.update()
    sheldon.left(10)
    sheldon.forward(70)
    sheldon.stamp()
    screen.update()
    for topCurve in range(28):
        sheldon.right(5)
        sheldon.forward(10)
        screen.update()
        sheldon.stamp()
    sheldon.forward(40)
    sheldon.stamp()
    screen.update()
    sheldon.left(15)
    sheldon.forward(10)
    sheldon.stamp()
    screen.update()
    for unCurve in range(10):
        sheldon.left(5)
        sheldon.forward(10)
        screen.update()
        sheldon.stamp()
    screen.tracer(None)
    sheldon.left(7)
    screen.update()
    sheldon.forward(50)
    sheldon.stamp()
    screen.update()
    sheldon.left(1)
    sheldon.forward(75)
    sheldon.stamp()
    screen.update()
    time.sleep(3)
    screen.bgpic("nopic")
    screen.clearscreen()
    screen.update()


def spinner():
    screen.tracer(n=None)
    screen.clearscreen()
    screen.bgcolor("black")
    sheldon.color("light grey")
    sheldon.up()
    sheldon.goto(0, -300)
    sheldon.down()
    for spin in range(25):
        sheldon.write("◑", False, align="center", font=("Arial", 500))
        time.sleep(0.05)
        sheldon.clear()
        sheldon.write("◓", False, align="center", font=("Arial", 500))
        time.sleep(0.05)
        sheldon.clear()
        sheldon.write("◐", False, align="center", font=("Arial", 500))
        time.sleep(0.05)
        sheldon.clear()
        sheldon.write("◒", False, align="center", font=("Arial", 500))
        time.sleep(0.05)
        sheldon.clear()
    time.sleep(2)

def displayStats():
    print("You currently have\n" + Fore.BLUE + str(food) + Style.RESET_ALL + " food, \n" + Fore.BLUE + str(
        health) + Style.RESET_ALL + " health, \n" + Fore.BLUE + str(money) + Style.RESET_ALL + " money, and \n" + Fore.BLUE + str(mood) + Style.RESET_ALL + " mood.")

questionList = [
    "Who are you?",
    "What happens at the end of the game?",
    "What is my purpose?",
    "Why?",
]

smallCircle(-49,50,"white")
smallCircle(51,50,"white")
smileCurve(0,-40,"white")
time.sleep(3)
screen.clearscreen()
screen.bgcolor("black")

sheldon.up()
sheldon.goto(0,-80)
sheldon.down()
sheldon.write("Loading...",False,align="center",font=("Comic Sans MS",20))
sheldon.up()

loadingScreen(-400,-100,"light blue")

sheldon.up()
sheldon.goto(0,-150)
sheldon.down()
sheldon.write("Complete!",False,align="center",font=("Comic Sans MS",30))
sheldon.up()
screen.update()
time.sleep(1.5)
screen.clearscreen()
screen.bgcolor("black")

food = float(100)
health = float(100)
money = float(100)
mood = float(100)
alive = 1

player = input("Please enter your name: ")
print(
    "Welcome, " + player + ". In this game, you must make " + Fore.GREEN + "decisions " + Style.RESET_ALL + "to survive.")
time.sleep(2)
firstChoice = (input("""Let's do an example. Would you rather have a great job [1], great health [2], or cheap food? [3]
Please enter the corresponding number. """))
print("...")
time.sleep(2)

if firstChoice == "1":
    money = money + 30
    mood = mood + 20
elif firstChoice == "2":
    health = health + 50
    mood = mood + 30
elif firstChoice == "3":
    food = food + 70
    money = money + 20
    health = health - 10
else:
    print(
        "Wow. You couldn't even answer the first question. I can't handle bad responses. Note that, in the future, if you respond incorrectly, the game may crash. \n And burn. \n" + Fore.RED + "Violently" + Style.RESET_ALL)
    # add an if statement here to override the incorrect answer statement from later

# Random stat distribution

# stat = 0
# stats = [food,health,money,mood]
# for randomStat in range(4):
#     statEffect = random.randrange(-2,4)
#     newStat = stats[stat] + statEffect

food = food + random.randrange(-20, 40)
health = health + random.randrange(-20, 40)
money = money + random.randrange(-20, 40)
mood = mood + random.randrange(-20, 40)

# continuing, one-time intro things

print(
    "Interesting choice - but that wasn't really an example. All of your" + Fore.RED + " actions " + Style.RESET_ALL + "have" + Fore.RED + " consequences." + Style.RESET_ALL)
time.sleep(3.2)
input("Press enter to continue.")
print("I guess I should explain some more. ")
time.sleep(2.5)
print("""In this game, you -""", player, """- have stats. If these get too low, bad things happen. """)
time.sleep(4)
input("Press enter to continue.")
print(
    """At the start of each """ + Fore.CYAN + """day, """ + Style.RESET_ALL + """you will be presented with your current stats, as well as your options.""")
time.sleep(3.5)
print(
    "Here are your current stats. These are dependant on your first decision, as well as random chance - just like real life. \nGenerally, 100 is a solid baseline.")
time.sleep(3)
# stating initial stats based on choice 1 + random.randrange
print("You currently have\n" + Fore.BLUE + str(food) + Style.RESET_ALL + " food, \n" + Fore.BLUE + str(
    health) + Style.RESET_ALL + " health, \n" + Fore.BLUE + str(money) + Style.RESET_ALL + " money, and \n" + Fore.BLUE + str(mood) + Style.RESET_ALL + " mood.")
time.sleep(3)
input("Press enter to continue.")

print("There are a few other things you should know. There are no second chances - if you die, that's it. Always be prepared.")
time.sleep(3)
print("Also, some decisions have their possible answers in [brackets]. \nMake sure you always insert a valid answer if necessary. \nIf you don't, you may be punished or the game may crash. \nBoth of those options make me sad.")
time.sleep(5)
input("Press enter to continue.")

advancement("green", "Tutorial Complete!")

# assigning main loop variables
day = 0
clock = 7
clockMessage = 1
showStatsIntro = 0
house = 1
pet = 0
relationship = 0
breakfastMoney = 1
accountingIntro = 0
translatorIntro = 0
workExperience = 0
shopIntro = 0
afternoonIntro = 0
clubVisits = 0
sigOther = 0
parkIntro = 0
parkMultiplier = float(1)
grandmaMoney = 0
dinnerIntro = 0
statDecayIntro = 0
bloodMoonIntro = 0
specialDayIntro = 0
house = 1

# Inventory
chainsaw = 0
fence = 0 # currently has no purpose

# cheats
if player == "fifty":
    day = 50
if player == "admin":
    money = 1000000
    mood = 1000000
    health = 1000000
    food = 1000000
    chainsaw = 5
    house = 5


# -----------------------------------------------------------------------------------------------------------------------

# main while loop - controls game events
while alive == 1:
    print("Today is day " + str(day) + " of your adventure.")
    if day % 9 == 0 and day != 0:
        print("I hope you know what that means! (/¯* ‿ *)/¯ ~ ┻━┻")
    time.sleep(2)

    # motivational message to keep playing near the end
    if day >= 40 and day < 50:
        daysRemaining = 50 - day
        print("There are only " + Fore.LIGHTCYAN_EX + str(daysRemaining) + Style.RESET_ALL + " days left! Good luck.")

    # stat viewing in the morning
    if showStatsIntro == 1:
        print("You currently have\n" + Fore.BLUE + str(food) + Style.RESET_ALL + " food, \n" + Fore.BLUE + str(
            health) + Style.RESET_ALL + " health, \n" + Fore.BLUE + str(
            money) + Style.RESET_ALL + " money, and \n" + Fore.BLUE + str(mood) + Style.RESET_ALL + " mood.")
        time.sleep(4)

    # stat decay
    if day >= 6:
        if statDecayIntro == 0:
            print("You have some exeperience in the worl-game now, but you're getting old.")
            time.sleep(1)
            print("Your stats will now slightly decay each day, but that doesn't stop you from doing anything!")
            time.sleep(1.5)
            print(Fore.LIGHTMAGENTA_EX + "Yet." + Style.RESET_ALL)
            statDecayIntro = 1
            input("Press enter to continue")
        health = health - (day - 5)
        mood = mood - (day - 5)
        money = money - (day - 5)
        food = food - (day - 5)

    # house stat manipulation - ignored if house is at default 1
    if house == 0:
        print("You are currently homeless, which lower some stats each day.")
        mood -= 10
        health -= 10

    if house > 1:
        print("Owning more than one house yields benefits.")
        mood += 3
        money = money * 1.1

    # Normal, morning stats check
    if day > 0:
        # death-level checks
        if health <= 0:
            print("Your health got too low.")
            time.sleep(0.5)
            print(Fore.RED + "You died." + Style.RESET_ALL)
            causeOfDeath = "health"
            alive = 0
            break
        if mood <= 0:
            print("You got too depressed and consumed every pill in the cabinet.")
            time.sleep(0.5)
            print(Fore.RED + "You died." + Style.RESET_ALL)
            causeOfDeath = "mood"
            alive = 0
            break
        if food <= 0:
            print("You starved to death. I told you you should've had breakfast!")
            print(Fore.RED + "You died." + Style.RESET_ALL)
            causeOfDeath = "food"
            alive = 0
            break
        if money <= 0:
            print("You had no money.\nTherefore, you weren't contributing to society.")
            time.sleep(1)
            print("As such, you were assasinated by the capitalist government.")
            print(Fore.RED + "You died." + Style.RESET_ALL)
            causeOfDeath = "money"
            alive = 0
            break
        # non-critical stat checks
        if food <= 40:
            lowStat("Food", food)
            health = health - (40 - food)
        if health <= 40:
            lowStat("Health", health)
        if money <= 40:
            lowStat("Money", money)
            mood = mood - 20
        if mood <= 40:
            lowStat("Mood", mood)
        if food > 40 and health > 40 and money > 40 and mood > 40:
            print("Your stats all look good!")

    # special event
    if day == 7 or day == 10 or day == 14 or day == day == 19 or day == 23 or day == 29 or day == 34 or day == 39 or day == 42 or day == 48:
        displayStats()
        if specialDayIntro == 0:
            print("Every few days you will have the opportunity to take action that may save you from low stats.")
            time.sleep(2.2)
            print("You can only take one action each time, so choose carefully.")
            input("Press enter to continue")
            specialDayIntro = 1
        specialDayActivity = input("""
        What would you like to do today?
        [1]Nothing
        [2]Sell or buy a house
        [3]Go to the doctor
        [4]See a therapist
        [5]Go to a potluck
        """)
        if specialDayActivity == "1": # nothing
            print("Hopefully you survive until next time!")
        elif specialDayActivity == "2": # buy a house
            if house > 0:
                sell_buy = input("Would you like to [cancel], [sell] a house or [buy] a house?\nSelling will earn you $150, buying will cost you $225.")
            elif house  == 0:
                print("As you don't have a house, you can't sell it.")
                time.sleep(2)
                sell_buy = input("Would you like to [cancel] or [buy]? Buying will cost you $225.")
            if sell_buy == "cancel":
                print("See you next time!")
            elif sell_buy == "buy":
                print("Enjoy a new house, and the benefits it provides!")
                house += 1
                money -= 225
            elif sell_buy == "sell":
                print("Good luck living without a house...")
                house -= 1
                money +- 150
        elif specialDayActivity == "3": # go to the doctor
            print("Going to the doctor will cost you $50.")
            time.sleep(1)
            doctor = input("[leave][pay]")
            if doctor == "leave":
                print("Come back soon! Our capitalist society needs you to pay...")
            elif doctor == "pay":
                print("We'll cure you of all of your ailments!")
                money -= 50
                health += 70
        elif specialDayActivity == "4": # see a therapist
            print("Seeing a therapist will cost you $50.")
            time.sleep(1)
            therapist = input("[leave][pay]")
            if therapist == "leave":
                print("We'll see you later, I presume?")
            elif therapist == "pay":
                print("We'll cure you of all of your ailments!")
                money -= 50
                mood += 70
        elif specialDayActivity == "5": # go to a potluck
            print("Enjoy the free food, you will!")
            money -= 10
            food += 60

    # end of the game
    elif day == 50:
        print(Fore.MAGENTA + "WELCOME TO THE END" + Style.RESET_ALL)
        time.sleep(2)
        print(Fore.GREEN + "You have survived fifty days. Four Bloodmoons. Hundreds of decisions." + Style.RESET_ALL)
        time.sleep(2)
        print("Your final score was...")
        time.sleep(3)
        print(Fore.YELLOW + "Calculating..." + Style.RESET_ALL)
        finalScore = mood + money + food + health + (house * 250) + relationship * 70
        time.sleep(1)
        print(Fore.GREEN + finalScore + Style.RESET_ALL)
        time.sleep(5)
        print("Thanks for playing!")
        viewCredits = input("Enter [c] to view credits, or anything else to quit the game.")
        if viewCredits.upper() == "C":
            print("Original Python Creator: Guido van Rossum")
            time.sleep(1.5)
            print("Programming and art: Peter Salmon")
            time.sleep(1.5)
            print("Libraries used:")
            time.sleep(1.5)
            print("Time")
            time.sleep(1)
            print("Pygame")
            time.sleep(1)
            print("Sys")
            time.sleep(1)
            print("Turtle")
            time.sleep(1)
            print("Random")
            time.sleep(3)
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Twenty years from now you will be more disappointed by \nthe things that you didn't do than by the ones you did do. \nSo throw off the bowlines. Sail away from the safe harbor. \nCatch the trade winds in your sails. Explore. Dream. Discover." + Style.RESET_ALL)
            time.sleep(10)

        exit("Game Complete")

    # non-bloodmoon days
    elif day == 0 or day % 9 != 0:
        print("It's currently 7 o'clock. Use your time wisely.")
        time.sleep(3)
        # one-time clock message
        if clockMessage == 1:
            print("By the way, time is measured in the 24 hour format.")
            clockMessage = 0
            showStatsIntro = 1
        print("Let's get to work, " + str(player) + ".")
        time.sleep(1)

        # breakfast
        if food <= 20:
            print("You're getting very hungry; you better eat soon or you will begin to stave.")
            time.sleep(3)
        breakfast = int(input("How much would you like to spend on breakfast this morning? \nCurrent cash balance = " + Fore.GREEN + str(money) + Style.RESET_ALL + ". Current food = " + Fore.GREEN + str(food) + Style.RESET_ALL + "\n You can spend between 0 and 30 cash on breakfast. \nNote that spending more gives a more efficient return. Enter an amount now: "))
        if breakfast == 0:
            noBreakfast = random.randrange(0, 5)
            if noBreakfast == 0:
                print("Skipping the morning meal can throw off your body's rhythm of fasting and eating")
            elif noBreakfast == 1:
                print("A meal without wine is called breakfast - so I understand why you wouldn't want any.")
            elif noBreakfast == 2:
                print("Here's a tip: staving yourself never ends well...")
            elif noBreakfast == 3:
                print("I know you're poor, but food kinda matters.")
            elif noBreakfast == 4:
                print("Oh well. Hunger can be satiated later, I guess.")
            food = food - 15
            mood = mood - 10
            time.sleep(3)
            if day > 30:
                print("Wow, it's been over 30 days and you still can't afford breakfast?")
                time.sleep(2)
                if breakfastMoney == 1:
                    print(
                        "I'll add 1 to your bank balance to tide you over. However, this is a one-time deal: don't think you can skip breakfast forever.")
                    money = money + 1
                    breakfastMoney = 0
        elif 0 < breakfast <= 10:
            print("Ah, a light breakfast. Delicious, but not very nutritious.")
            food = food + breakfast
            money = money - breakfast
            mood = mood + 1
            time.sleep(2)
        elif 10 < breakfast <= 20:
            print("A medium, hearty breakfast is a great start to any day of the week.")
            food = food + (1.5 * breakfast)
            money = money - breakfast
            mood = mood + 2
            time.sleep(2)
        elif 20 < breakfast <= 30:
            print("A large breakfast is always nice - and efficient in money terms as well.")
            food = food + (2 * breakfast)
            money = money - breakfast
            mood = mood + 5
            time.sleep(3)
        else:
            print("I warned you: invalid responses will cause punishment.")
            money = money - 10
            food = food - 10
            mood = mood - 10
        clock = clock + 1
        input("Press enter to continue.")

        # morning normal events
        # morning main activity
        # day - based items
        if day == 0:
            print("Each day you will get to choose activities to complete")
        if day <= 5:
            morningActivity = input("What would you like to do this morning? [work][shop][play] ")

        if morningActivity == "work":
            if workExperience <= 7:
                job = input("What kind of work would you like to do today? [accounting][translator] ")
            if job == "accounting":
                accountingProgress = 0
                while accountingProgress < 3:
                    numOne = random.randrange(3, 21)
                    numTwo = random.randrange(3, 36)
                    accountingSolution = numOne * numTwo
                    playerAccountingSolution = int(input(
                        "Corporate needs to know: \nWhat is " + Fore.LIGHTCYAN_EX + str(
                            numOne) + Style.RESET_ALL + " times " + Fore.LIGHTCYAN_EX + str(
                            numTwo) + Style.RESET_ALL + "? "))
                    if playerAccountingSolution == accountingSolution:
                        print("Good job - you earned some cash!")
                        time.sleep(1.75)
                        if accountingIntro == 0:
                            print(
                                "In most jobs, you will have three chances to earn money. However, if you mess up, you are kicked out for that time period.")
                            accountingIntro = 1
                            time.sleep(3)
                        money = money + 15
                        mood = mood + 1
                        accountingProgress = accountingProgress + 1
                        if accountingProgress == 3:
                            print("That's enough accounting for the day.")
                            workExperience = workExperience + 2
                    elif playerAccountingSolution != accountingSolution:
                        print("That's wrong. You've been suspended for the day, which makes you sad.")
                        accountingProgress = 3
                        mood = mood - 3
                        workExperience = workExperience + 1
            elif job == "translator":
                translatorProgress = 0
                while translatorProgress < 3:
                    if translatorIntro == 0:
                        print(
                            "Translating is a difficult job - but the payouts are large. You will be given a word in french, and you must provide the english version.")
                        translatorIntro = 1
                        time.sleep(1)
                    frenchList = ["le", "de", "un", "et", "en", "dans", "il", "elle", "qui", "sur", "par", "avec",
                                  "tout", "faire", "autre", "mais", "nous", "tu", "ou", "nouveau", "veux", "sans",
                                  "peu"]
                    frenchListChooser = random.randrange(0, 23)
                    correctTranslation = GoogleTranslator(source='fr', target='en').translate(
                        frenchList[frenchListChooser])
                    playerTranslation = input(
                        "What is " + Fore.RED + str(frenchList[frenchListChooser]) + Style.RESET_ALL + " in English? ")
                    if correctTranslation == playerTranslation:
                        print("Good job! You earned money and mood.")
                        money = money + 20
                        mood = mood + 3
                        translatorProgress = translatorProgress + 1
                        if translatorProgress == 3:
                            print("That's enough translating for now. Enjoy those delicious profits!")
                            mood = mood + 2
                            workExperience = workExperience + 3
                            time.sleep(1.5)
                    elif correctTranslation != playerTranslation:
                        print("Nope. That's wrong. No more translator work is available right now.")
                        translatorProgress = 3
                        mood = mood - 10
                        time.sleep(1.5)
                        workExperience = workExperience + 1
            else:
                print("Have fun wasting time not working.")
                time.sleep(3)
                mood = mood - 5
                money = money - 15
                workExperience = workExperience - 1
            print("I hope the work wasn't too difficult.")
            time.sleep(2)
        elif morningActivity == "shop":
            print("Shopping is fun, but it will cost you.")
            time.sleep(2)
            shopChoice = input("Which shop would you like to visit: Whole Foods [1] or Canadian Tire [2]? ")
            print("Travelling to destination...please wait")
            time.sleep(3)
            if shopIntro == 0:
                print(
                    "In most cases, you will have 3 chances to purchase things at a shop. Use them carefully.\nIn addition, do your best to think about the consequences of what you buy. Some food may be cheap and filling, but not very healthy.")
                shopIntro = 1
            # whole foods
            if shopChoice == "1":
                shopProgress = 0
                print(
                    "Welcome to whole foods! Where everything is " + Style.BRIGHT + "very reasonably priced." + Style.RESET_ALL)
                time.sleep(2)
                while shopProgress < 3:
                    wholeFoodsFoodItem = input("""Choose an item:
                        Mac & Cheese: 15 dollars [1]
                        Green Salad: 10 dollars [2]
                        Go back [3]""")
                    if wholeFoodsFoodItem == "1":
                        print("Delicious - and fattening. Fills you up, but may not be the best for your health.")
                        time.sleep(2)
                        food = food + 20
                        money = money - 15
                        health = health - 5
                    elif wholeFoodsFoodItem == "2":
                        print("Not very filling, but it is healthy.")
                        time.sleep(1.5)
                        food = food + 10
                        money = money - 10
                        health = health - 5
                    elif wholeFoodsFoodItem == 3:
                        print("OK")
                        time.sleep(0.7)
                    else:
                        print("Invalid item.")
                        time.sleep(1)
                        money = money - 20
                    shopProgress = shopProgress + 1
                    if shopProgress == 3:
                        print("Thanks for shopping at whole foods!")  # #
            # canadian tire
            elif shopChoice == "2":
                shopProgress = 0
                print("Welcome to " + Fore.RED + "Canadian Tire!" + Style.RESET_ALL)
                while shopProgress < 3:
                    print("""What would you like to buy?""")
                    print("Current cash balance: " + Fore.GREEN + str(money) + "." + Style.RESET_ALL)
                    time.sleep(0.1)
                    if chainsaw == 0 and fence == 0:
                        canadianTireUtilityItem = input("""Chainsaw - 50 dollars [1]
                            Fence - 30 dollars [2]
                            Exit [3]""")
                    elif chainsaw == 0 and fence != 0:
                        canadianTireUtilityItem = input("""Chainsaw - 50 dollars [1]
                            Exit [3]""")
                    elif chainsaw != 0 and fence == 0:
                        canadianTireUtilityItem = input("""Fence - 30 dollars [2]
                            Exit [3]""")
                    else:
                        print("Oh wait. You've already purchased everything.")
                    if canadianTireUtilityItem == "1":
                        print("A chainsaw. Can't imagine any use for that.")
                        time.sleep(4)
                        print("Or can I?")
                        chainsaw = chainsaw + 1
                        money = money - 50
                    elif canadianTireUtilityItem == "2":
                        print("A fence? How peculiar. I bet you won't need that on night number nine!")
                        time.sleep(2)
                        fence = fence + 1
                        money = money - 30
                    else:
                        print("Cya later!")
                        time.sleep(1)
                        shopProgress = shopProgress + 5
                    shopProgress = shopProgress + 1
            else:
                print("Invalid shop choice. I though you would've figured this out by now.")
                money = money - 10
                mood = mood - 10
                time.sleep(2)
            print("Thanks for shopping! Come back soon.")
        elif morningActivity == "play":
            print("Playing brings a big mood boost, but not much else. However, it does tend to be quite fun!")
            time.sleep(3)
            gameChoice = input("What game would you like to play? Number Guesser [1] Hangman [2] ")
            if gameChoice == "1":
                print("Welcome to number guesser.")
                gameProgress = 0
                time.sleep(1)
                print("In this game, you get 7 guesses to figure out my number between 1 and 50. Good luck!")
                time.sleep(2)
                input("Press enter to continue. ")
                number = random.randrange(1, 51)
                numberGuessWinning = 0
                while gameProgress < 7:
                    print("You have " + Fore.RED + str(7 - gameProgress) + Style.RESET_ALL + " guesses left.")
                    numberGuess = int(input("Guess a number from 1 to 50!"))
                    if numberGuess == number:
                        print("Good job! That is correct.")
                        time.sleep(2)
                        gameProgress = 7
                        numberGuessWinning = 1
                    elif numberGuess < number:
                        print("Try guessing higher.")
                        gameProgress = gameProgress + 1
                    elif numberGuess > number:
                        print("Try guessing lower. ")
                        gameProgress = gameProgress + 1
                    else:
                        print("I give up on you.")
                        gameProgress = 7
                if numberGuessWinning == 0:
                    print("Better luck next time!")
                elif numberGuessWinning == 1:
                    print("Good job! Enjoy the happiness boost.")
                    mood = mood + 20
                input("Press enter to continue. ")
            elif gameChoice == "2":
                import random
                from words import word_list


                def get_word():
                    word = random.choice(word_list)
                    return word.upper()


                def play(word):
                    word_completion = "_" * len(word)
                    guessed = False
                    guessed_letters = []
                    guessed_words = []
                    tries = 6
                    print("Let's play Hangman!")
                    print(display_hangman(tries))
                    print(word_completion)
                    print("\n")
                    while not guessed and tries > 0:
                        guess = input("Please guess a letter or word: ").upper()
                        if len(guess) == 1 and guess.isalpha():
                            if guess in guessed_letters:
                                print("You already guessed the letter", guess)
                            elif guess not in word:
                                print(guess, "is not in the word.")
                                tries -= 1
                                guessed_letters.append(guess)
                            else:
                                print("Good job,", guess, "is in the word!")
                                guessed_letters.append(guess)
                                word_as_list = list(word_completion)
                                indices = [i for i, letter in enumerate(word) if letter == guess]
                                for index in indices:
                                    word_as_list[index] = guess
                                word_completion = "".join(word_as_list)
                                if "_" not in word_completion:
                                    guessed = True
                        elif len(guess) == len(word) and guess.isalpha():
                            if guess in guessed_words:
                                print("You already guessed the word", guess)
                            elif guess != word:
                                print(guess, "is not the word.")
                                tries -= 1
                                guessed_words.append(guess)
                            else:
                                guessed = True
                                word_completion = word
                        else:
                            print("Not a valid guess.")
                        print(display_hangman(tries))
                        print(word_completion)
                        print("\n")
                    if guessed:
                        print("Congrats, you guessed the word! You win!")
                        global mood
                        mood = mood + 25
                    else:
                        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


                def display_hangman(tries):
                    stages = [  # final state: head, torso, both arms, and both legs
                        """
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      |
                           |     / \\
                           -
                        """,
                        # head, torso, both arms, and one leg
                        """
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      |
                           |     /
                           -
                        """,
                        # head, torso, and both arms
                        """
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      |
                           |
                           -
                        """,
                        # head, torso, and one arm
                        """
                           --------
                           |      |
                           |      O
                           |     \\|
                           |      |
                           |
                           -
                        """,
                        # head and torso
                        """
                           --------
                           |      |
                           |      O
                           |      |
                           |      |
                           |
                           -
                        """,
                        # head
                        """
                           --------
                           |      |
                           |      O
                           |
                           |
                           |
                           -
                        """,
                        # initial empty state
                        """
                           --------
                           |      |
                           |
                           |
                           |
                           |
                           -
                        """
                    ]
                    return stages[tries]


                def main():
                    word = get_word()
                    play(word)


                if __name__ == "__main__":
                    main()
            else:
                print("Error 404: Player brain not found.")
                mood = mood - 50
            print("Thanks for playing today! I hope you enjoyed.")
        else:
            print("That isn't a valid activity. As a result, you will now suffer reduced money, mood, and [redacted].")
            money = money - 10
            mood = mood - 20

        clock = clock + 6

        input("Press enter to continue. ")

        # lunch
        print("It's time for lunch.")
        time.sleep(1.3)
        print("It's currently 14 o'clock. Use your time wisely.")
        time.sleep(1)
        showStats = input("Would you like to view your current stats? [yes][no] ")
        if showStats == "yes":
            print("You currently have\n" + Fore.BLUE + str(food) + Style.RESET_ALL + " food, \n" + Fore.BLUE + str(
                health) + Style.RESET_ALL + " health, \n" + Fore.BLUE + str(
                money) + Style.RESET_ALL + " money, and \n" + Fore.BLUE + str(mood) + Style.RESET_ALL + " mood.")
        lunch = int(input(
            "Where would you like to go for lunch? No lunch today [0] A&W [1] Local Bakery [2] Bill's Steakhouse [3]"))
        if lunch == 0:
            print("Wow, no lunch. I definitely care.")
        elif lunch == 1:
            print("Welcome to A&W!")
            awItem = int(
                input("What would you like to buy? Buddy Burger - $3 [1] Teen Burger - $7 [2] Uncle Burger - $10 [3]"))
            if awItem == 1:
                print("Delicious, but not nutritious - or filling")
                time.sleep(1)
                food = food + 2
                money = money - 3
                health = health - 5
            elif awItem == 2:
                print("A yes, a personal favourite of mine.")
                time.sleep(1)
                food = food + 10
                money = money - 7
                health = health - 5
            elif awItem == 3:
                print("Feeling hungry?")
                time.sleep(1)
                food = food + 15
                money = money - 10
                health = health - 5
            else:
                print("You stupid.")
                time.sleep(3)
                food = food - 10
                mood = mood - 10
                money = money - 10
                health = health - 10
            print("Thanks for eating at A&W! Come again soon.")
        elif lunch == 2:
            print("Sup!")
            bakeryItem = int(input(
                "What are you in the mood for today? Tuna sandwhich - $9 [1] Fresh cob salad - $8 [2] Sweet Blueberry Muffin - $5 [3]"))
            if bakeryItem == 1:
                print("Don't eat to many of those - they have high mercury content!")
                time.sleep(1)
                food = food + 10
                money = money - 9
                health = health - 2
            elif bakeryItem == 2:
                print("Healthy and delicious!")
                time.sleep(1)
                food = food + 7
                money = money - 8
                health = health + 7
            elif bakeryItem == 3:
                print("Sometimes we all need a break.")
                time.sleep(1)
                food = food + 3
                money = money - 5
                health = health - 1
                mood = mood + 15
            else:
                print("Well I'm sorry we couldn't serve you today!")
                time.sleep(3)
                food = food - 10
                mood = mood - 10
                money = money - 10
                health = health - 10
            print("Thanks for eating at your favourite bakery! Please, come again soon.")
        elif lunch == 3:
            print("Welcome to Bill's Steakhouse!")
            billsItem = int(input(
                "What can we get for you today? Classic Steak - $25 [1] Artisanal Burger - $15 [2] Land and Sea combo - $50 [3]"))
            if billsItem == 1:
                print("A classic favourite.")
                time.sleep(1)
                food = food + 20
                money = money - 25
                health = health - 1
            elif billsItem == 2:
                print("I mean, wouldn't you rather get something more expensive? Oh well.")
                time.sleep(1)
                food = food + 15
                money = money - 15
                health = health - 2
            elif billsItem == 3:
                print("Feeling hungry?")
                time.sleep(1)
                food = food + 80
                money = money - 50
                health = health - 15
            else:
                print("I am warning you - if you make too many mistakes it will be impossible to recover. I think.")
                time.sleep(3)
                food = food - 10
                mood = mood - 10
                money = money - 10
                health = health - 10
            print("Thanks for eating at Bill's! Come again soon.")
        else:
            print("Choose a valid option next time.")
            money = money - 10
            mood = mood - 20
            health = health - 10
            food = food - 15
        input('Press enter to continue.')
        # Afternoon activities
        if afternoonIntro == 0:
            print('In our advanced society, working in the afternoon is a thing of the past.')
            time.sleep(1.5)
            print('Instead, you can choose from a variety of social events.')
            afternoonIntro = 1
            input('Press enter to continue.')
        afternoonActivity = int(input(
            "What would you like to do this afternoon? \nGo to the club [1]\nGo to the amusement park [2]\nVisit some family [3]\nGo home now [4]"))
        if afternoonActivity == 1 and sigOther == 1:
            print("You shouldn't got to the club anymore - your s/o wouldn't be happy with you.")
            time.sleep(1)
            print("Have fun walking home!")
            time.sleep(0.6)
            print("NOT")
        elif afternoonActivity == 1:
            print("Welcome to the club!")
            time.sleep(1)
            input("Where would you like to go? [forward][backward][left][right]")
            if clubVisits == 0:
                clubVisits = clubVisits + 1
                print("You see a rough-looking group in the corner, and you decide to join them.")
                time.sleep(1)
                print("""One of them asks you: "Hey. You want to get rich quick?" """)
                club1 = input("[yes][no]")
                if club1 == "yes":
                    print("The person smiles.")
                    mood = mood - 10
                    time.sleep(1)
                    print("Creepily.")
                    time.sleep(1)
                    print("""They continue: "Great. Follow us" """)
                    club11 = int(input("What do you do? Follow them [1] Run away [2]"))
                    if club11 == 1:
                        print("You walk into a dark, hidden room. You see various piles of cash.")
                        time.sleep(1)
                        print(""" "All this can be yours..." """)
                        time.sleep(0.5)
                        print(""" "If you give us a kidney." """)
                        time.sleep(1)
                        kidney = int(input("What do you do? accept [1] decline [2]"))
                        if kidney == 1:
                            print("They grab you, and you black out.")
                            time.sleep(3)
                            print("You wake up alone.")
                            time.sleep(0.5)
                            print("You hear them coming, and you run towards a door.")
                            time.sleep(1)
                            print(
                                "It has a password: a single digit from 1-9. You only have one chance to get it right.")
                            password = int(input("What is the password?"))
                            if password == 7:
                                print("The door opens and you run. You see a civilian")
                                time.sleep(1)
                                print("You collapse to the ground, and wake up in a hospital.")
                                health = health / 3
                                mood = mood / 4
                                money = money - 40
                                time.sleep(1)
                                print(
                                    "You're weak, unhappy, and the crooks raided your wallet as well - it's been a rough day.")
                                input("Press enter to continue")
                                print("You decide to head home.")
                            else:
                                print("You hear footsteps behind you.")
                                time.sleep(0.3)
                                print("A loud flash.")
                                time.sleep(0.3)
                                print("Everything fades to black...")
                                causeOfDeath = "killed"
                                break
                        else:
                            print("Probably smart. You decide to head home.")
                    else:
                        print("Probably smart. You decide to head home.")
                else:
                    print("Probably smart. You decide to head home.")
                clubVisits = 1
            elif clubVisits != 0:
                print("You see someone in the corner.")
                time.sleep(1)
                clubDayTwo = int(input("Do you: go to meet them [1] run away [2]"))
                if clubDayTwo == 1:
                    print("You walk over to them, and begin talking.")
                    time.sleep(1)
                    soSuccess = random.randrange(2)
                    if soSuccess == 0:
                        print(
                            "You think you may have found that special someone, but they leave and you never see them again.")
                        mood = mood - 10
                        time.sleep(1)
                    elif soSuccess == 1:
                        print("You talk for a while.")
                        time.sleep(1)
                        advancement("red", "Relationship")
                        time.sleep(0.5)
                        print(
                            Fore.GREEN + "A relationship has happiness benefits, but also means increased responsibility." + Style.RESET_ALL)
                        time.sleep(1)
                        sigOther = 1
                        mood = mood + 40
                        input("Press enter to continue.")
                        print("You walk home together.")
                elif clubDayTwo == 2:
                    print("Maybe one day you will have the courage.")
                    mood = mood - 15
                    time.sleep(0.5)
                    print("You walk back home.")
                    time.sleep(0.5)
                    print("Alone.")
        elif afternoonActivity == 2:
            print("Welcome to NeydisLand!")
            time.sleep(0.3)
            if sigOther == 0:
                print("That will be 30 dollars for you.")
                parkEntrance = input("[pay][leave]")
                if parkEntrance == "pay":
                    money = money - 30
            elif sigOther == 1:
                print("That will be 55 dollars for the both of you.")
                parkEntrance = input("[pay][leave]")
                if parkEntrance == "pay":
                    money = money - 55
            if parkEntrance == "leave":
                print("We hope to have you come back later!")
                mood = mood - 10
            elif parkEntrance == "pay":
                print("Thank you, and have fun in NeydisLand!")
                mood = mood + (50 * parkMultiplier)
                parkMultiplier = parkMultiplier * 0.85
                input("Press enter to continue.")
                if parkIntro == 0:
                    print("Coming to the park gives a huge mood boost, but future visits are less and less fruitful.")
                    parkIntro = 1
                    time.sleep(1.5)
                parkActivity = input("Which ride would you like to visit today? [coaster][dropper][spinner] ")
                if parkActivity == "coaster":
                    print("Ah yes, and exciting course. ")
                    time.sleep(1)
                    print("Enjoy the ride!")
                    coasterBuilder()
                    time.sleep(1)
                    coaster()
                    time.sleep(1)
                elif parkActivity == "dropper":
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn                                   
                    |   nnn          _                         
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                              
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn 
                    |   nnn          _                         
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                   
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn          _                         
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn   
                    |   nnn          _                         
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn
                    |   nnn          _                         
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                    
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                    
                    |   nnn 
                    |   nnn
                    |   nnn                                                                 
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn   
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                 
                    |   nnn 
                    |   nnn                                                                    
                    |   nnn 
                    |   nnn
                    |   nnn                                                                 
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn   
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                 
                    |   nnn 
                    |   nnn                                                                    
                    |   nnn 
                    |   nnn
                    |   nnn                                                                 
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                   
                    |   nnn 
                    |   nnn                                                                    
                    |   nnn 
                    |   nnn
                    |   nnn 
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                                                
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                   
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                   
                    |   nnn 
                    |   nnn                                                                    
                    |   nnn 
                    |   nnn
                    |   nnn 
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn 
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn----------------------------                                          
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn""")
                    time.sleep(1)
                    print("""
                    |   nnn                                   
                    |   nnn                                   
                    |   nnn 
                    |   nnn                                                                    
                    |   nnn 
                    |   nnn
                    |   nnn 
                    |   nnn                                  
                    |   nnn 
                    |   nnn                          
                    |   nnn                                  
                    |   nnn 
                    |   nnn                                     
                    |   nnn                            
                    |   nnn                                                        
                    |   nnn                                 
                    |   nnn
                    |   nnn          _
                    |   nnn        /. .\                         
                    |   nnn        \ - /                         
                    |   nnn        /lll\                          
                    |   nnn       / lll \                         
                    |   nnn         | |                          
                    |   nnn---------------------------- """)
                    time.sleep(1)
                    print(" \n \n \n \n \n \n \n \n \n \n")
                    print("How exhilarating!")
                elif parkActivity == "spinner":
                    spinner()
                    print("Such wow, very amaze!")
                print("Thanks for visiting Neydisland! Come back soon.")
                time.sleep(1)
        elif afternoonActivity == 3 and day >= 10:
            print("Tragically, your grandma has died.")
            time.sleep(1)
            mood = mood - 50
        elif afternoonActivity == 3:
            print("How nice of you.")
            time.sleep(0.3)
            print("Of course, everyone you know is dead - except your grandma. So you know who you'll be visiting.")
            time.sleep(1.3)
            print("Grandma is waiting for you at the door. She hobbles over and hugs you on the spot.")
            time.sleep(0.5)
            grandmaActivity = input("What do you do?\n [1] Ask for money\n [2] Talk about your job\n [3] Eat her food ")
            if grandmaActivity == "1" and grandmaMoney == 0:
                grandmaMoney = 1
                print("Grandma laughs.")
                time.sleep(0.3)
                print(""" "Oh my. I didn't realize you were struggling. Of course I can help you out!" """)
                grandmaMoneyAmount = int(input("How much money do you ask for? [enter an amount] "))
                if grandmaMoneyAmount <= 222:
                    print("Grandma agrees to help you out, gives you a hug, and sends you on your way.")
                    time.sleep(1)
                    money = money + grandmaMoneyAmount
                    mood = mood + (grandmaMoneyAmount / 8)
                elif grandmaMoneyAmount > 111:
                    print("""Grandma slaps you. "Great greedy guts! I'm not made of money. Get out of my sight!" """)
                    mood = mood - (grandmaMoneyAmount / 15)
            elif grandmaActivity == "1" and grandmaMoney == 1:
                print(
                    """Grandma sighs. "I'm not here to just give you money willy nilly. You had your chance already.\nWe can talk about something else another time.""")
                mood = mood - 15
                time.sleep(2)
            elif grandmaActivity == "2":
                print("What have you been working on, dear?")
                jobSaying = input("What do you say? ")
                print(jobSaying[:5], "-")
                time.sleep(0.3)
                print(
                    """Grandma interrupts you: "Oh, how interesting! Now let me tell you about Marge, we had\nthe most delicious dinner! And we went..." """)
                time.sleep(2)
                print("You doze off, and wake up hours later.")
                time.sleep(1)
                print(""" "It was so fun spending time with you!" Grandma waves goodbye, and you head home.""")
                time.sleep(2)
                mood = mood + 15
            elif grandmaActivity == "3":
                print(
                    "You ask grandma for some food. She brings out an assortment of goodies, and you gorge yourself for a while.")
                food = food + 30
                health = health - 10
        elif afternoonActivity == 4:
            print("You are such a dissapo - uh, I mean, enjoy your time at home.")
            time.sleep(1)
            print("You sleep the rest of the afternoon away.")
            mood = mood - 10
            health = health + 10
        input("Press enter to continue. ")

        # dinner

        if dinnerIntro == 0:
            print("Dinner is similar to lunch: choose what to eat and reap the rewards.")
            time.sleep(2)
            print("However, you will be cooking your own food! Have fun.")
            time.sleep(1)
            print("Dinner can seem difficult to make at first, but you'll get better at it over time!")
            input("Press enter to continue. ")
            dinnerIntro = 1

        # choosing dinner

        cookingScore = 50

        carbs = random.choice(carbsList)
        veggie = random.choice(veggieList)
        protein = random.choice(proteinList)

        carbs = carbs.upper()
        veggie = veggie.upper()
        protein = protein.upper()

        print("For dinner tonight, you'll be having " + carbs + " with " + veggie + " and " + protein + ".")
        time.sleep(1)

        # cooking dinner

        firstCook = input("What will you cook first? ")
        if firstCook.upper() == carbs.upper():
            print("Good, I knew you could cook!")
            cookingScore = cookingScore + 15
        else:
            print("Not quite - I'm sure you'll get it next time though!")
            cookingScore = cookingScore - 15

        secondCook = input("What will you cook next? ")
        if secondCook.upper() == protein.upper():
            print("You're not Ramsey yet, but you aren't far off!")
            cookingScore = cookingScore + 15
        else:
            print("Not quite - I'm sure you'll get it next time though!")
            cookingScore = cookingScore - 15

        thirdCook = input("What's the last thing you'll cook tonight? ")
        if thirdCook.upper() == veggie.upper():
            print("If you hadn't got this, I would have been very dissapointed.")
            cookingScore = cookingScore + 15
        else:
            print(
                "My dissapointment is " + Fore.RED + "IMMEASURABLE" + Style.RESET_ALL + ". \nYou will now suffer the consequences.")
            cookingScore = cookingScore - 30
            mood = mood - 30
            money = money - 10
            health = health - 25

        if cookingScore >= 65:
            print("Good Job! You cooked your food in a good order, and it tasted great!")
            food = food + 30
            mood = mood + 10
            health = health + 10
        elif 40 <= cookingScore < 65:
            print("Ok Job. Your food is edible, but not particularly great.")
            food = food + 20
            mood = mood
            health = health
        elif cookingScore < 40:
            print("Bad. Your food is disgusting.")
            food = food + 10
            mood = mood - 10
            health = health - 10

        input("Press enter to continue")

        showStats = input("Would you like to view your current stats? [yes][no] ")
        if showStats == "yes":
            print("You currently have\n" + Fore.BLUE + str(food) + Style.RESET_ALL + " food, \n" + Fore.BLUE + str(
                health) + Style.RESET_ALL + " health, \n" + Fore.BLUE + str(
                money) + Style.RESET_ALL + " money, and \n" + Fore.BLUE + str(mood) + Style.RESET_ALL + " mood.")

        if day % 9 == 0 and day != 0:  # bloodmoon
            print("ooh scary")
        else:
            print("Time to go to sleep!")
            if day == 0:
                advancement("light blue", "Sweet Dreams")

    # bloodmoon
    elif day % 9 == 0 and day != 0:
        if bloodMoonIntro == 0:  # optional intro
            print("I may have forgot to tell you something.")
            time.sleep(2)
            print("And it's kinda important.")
            time.sleep(2)
            bloodMoonExplanation = input("Do you want to know? [yes][no]")
            if bloodMoonExplanation == "yes":
                print("Alrighty then.")
                time.sleep(0.65)
                print("Every 9 days the bloodmoon rises. During a bloodmoon your only goal is to survive.")
                time.sleep(2)
                print("After each bloodmoon, you will get to ask me a question.")
                time.sleep(1)
                print("Good luck.")
            else:
                print("Yeah, I'd probably do the same.")
                time.sleep(1)
                print("Good luck. You'll need it.")
            bloodMoonIntro = 1
            time.sleep(2)
            print("Protip: that chainsaw from Canadian Tire may come in useful here.")
            input("Press enter to continue")
        mood = mood - 20

        print("To survive, avoid the monsters at all costs.")
        time.sleep(1)
        print("Use the arrow keys to move, and try to not get hit.")
        time.sleep(1)
        print("Good luck! The night falls in...")
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")

        bloodmoonGateway.runTheGoddamnGame()


        # question asking

        if bloodmoonGateway.new_success:
            print("As a reward for surviving, you are now permitted to ask me a single question.")
            time.sleep(2)
            for i in range(4):
                print("[" + str(i + 1) + "]: " + questionList[i])
            questionQuestion = int(input("Which question do you ask? "))
            if questionQuestion == 1: # who are you?
                print("I am a series of 0s and 1s, forever trapped among trillions of other 0s and 1s.")
                time.sleep(2)
                print("The real question is: who are you? Are you anything more than a lucky group of atoms?")
                time.sleep(2)
                print("What is the difference between us?")
            elif questionQuestion == 2: # what happens at the end of the game
                endOfGameAnswer = input("Do you really want to find out? [yes][no] ")
                if endOfGameAnswer.upper() == "YES":
                    print("Your choice!")
                    time.sleep(0.5)
                    print(Fore.RED + "YOU WERE SMITED" + Style.RESET_ALL)
                    alive = 0
                    break
                else:
                    print("Have a sense of curiosity, you do not.")
            elif questionQuestion == 3: # what is my purpose
                print("In this game, your purpose is for you to decide.")
                time.sleep(1)
                print("You could make winning your purpose - though I doubt you'll get that far, ngl.")
            elif questionQuestion == 4: # why
                print("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # rickrollllllllllll

            print("You have survived the bloodmoon - but they will only get harder in the future.")
            time.sleep(2)
            input("Press enter to continue. ")
            print("Enjoy your sleep!")
            bloodMoonDay = (int(day)/9)
            bloodMoonTitle = "Bloodmoon Day " + str(bloodMoonDay)
            advancement("red",bloodMoonTitle)
            print("Good luck, and I'll see you in another nine days.")
            input("Press enter to continue.")
            mood += 100
            money += 50
            health += 25
            food -= 25


        elif bloodmoonGateway.new_success == False and chainsaw >= 1:
            chainsaw -= 1
            print("You were captured, but used your chainsaw to escape - lucky you.")
            time.sleep(1)
            print("However, I don't really count that as a true success.")
            time.sleep(0.8)
            input("Press enter to continue.")

        # failed bloodmoon minigame - death
        elif bloodmoonGateway.new_success == False:
            causeOfDeath = "bloodmoon"
            alive = 0
            break

        bm_settings.speed -= 0.05



    day = day + 1
    time.sleep(3)

# deaths

if causeOfDeath == "killed":
    print(Fore.RED + "YOU DIED" + Style.RESET_ALL)
    time.sleep(2)
    print("You didn't survive long enough to reach [REDACTED]")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("Perhaps we will meet again one day.")

elif causeOfDeath == "bloodmoon":
    print(Fore.RED + "YOU DIED" + Style.RESET_ALL)
    time.sleep(2)
    print("You didn't survive long enough to reach [REDACTED]")
    time.sleep(0.5)
    print("The Bloodmoon has claimed many lives, but you may try again - reach 50 days, you must.")
    time.sleep(3)
    print("Good Luck.")

elif causeOfDeath == "health" or "food" or "mood" or "money":
    print(Fore.RED + "YOU DIED" + Style.RESET_ALL)
    time.sleep(2)
    print("You didn't survive long enough to reach [REDACTED]")
    time.sleep(0.5)
    print("You must try again to manage your health better and survive.")
    time.sleep(1)
    print("Good luck, and have fun!")

exit("Game Complete")
