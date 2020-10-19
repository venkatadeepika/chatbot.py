"""
specifation of the chat bot:
1. This bot will start with a greet and introduce itself and the ask the users name for greeting.
2. This bot will suggest a user to select a mobile accodring their choice of prefernce.
3. The bot will ask the user for there choice to suggest them the appropriate model.
4. It will respond to user input appropriate to suggest the best model.

"""

import random

def introduction():
    responses =[
        "Hello Iam a technical friendly bot and will help you to select a mobile model based on your prefernce.",
        "Welcome!!!!, Iam bot. I will help you to choose your mobile ma\odel based on your prefernce."
    ]
    print(random.choice(responses))


def interaction(name):
    messages = [
        "Thank you. Pleasure to meet you.",
        "Lets have nice time togther."
    ]
    print(random.choice(messages))
    print("________")


def bot_features():
    print("--->This bot will suggesr a user to select a mobile model according their basic choice of prefernce.")
    print("--->The bot will ask the user for their choice to suggest them the appropriate model.")
    print("--->It will respond to user input appopriatly to suggest the best model.")
    print("________")


def mobile_model():
    ram = int(input("Enter your RAM requirement 4GB, 6GB, 8GB OR 12GB: "))
    processor = int(input("Enter processor type snap dragon :665, 710, 720 OR 855+ : "))

    if ram == 6 or ram == 12  and processor == 665:
        print("Available mobile models with that specifation is Realme 7i series.")
        print("________")

    elif ram == 8 and processor == 855:
        print("Available mobile models with that specifation is Realme X3 super zoom series.")
        print("________")

    elif ram == 12 and processor == 720:
        print("Available mobile models with that specifation is Realme X2 series.")
        print("________")

    elif ram == 6 and processor == 710:
        print("Available mobile models with that specifation is Realme X series.")
        print("________")
    else:
        print("Please enter the valid input: ")
        print("________")



def show_menu():
    print("Please select choice from the below.")
    print("1.know about me and my features(bot).")
    print("2.Know your mobile models available based on your prefrences.")
    print("3.End the chat if your got the model of your model.")
    print("________")
    try:
        return int(input("Enter your choise from"))
    except:
        print("Enter choice only from 1,2,3.")
        return 0



def bot():
    introduction()
    name = input("May i know your name please : ")
    interaction(name)
    response = show_menu()
    while response != 3:
        if response == 1:
            bot_features()
        elif response == 2:
            mobile_model()
        else:
            print("I don't understand that.Please enter a valid input from the given choice.")
        response = show_menu()
