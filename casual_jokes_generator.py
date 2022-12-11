#CASUAL JOKES GENERATOR:

#Import the random module.
import random

#Create a list of jokes.
jokes_sentences = ["Chocolate does not ask any questions. Chocolate simply understands.",
                   "As long as cocoa beans grow on trees, chocolate is fruit to me.",
                   "I’m jealous of my parents, I’ll never have a kid as cool as them.",
                   "Stupidity knows no boundaries, but it knows a lot of people.",
                   "The best part of going to work is coming back home at the end of the day.",
                   "I’m not lazy. I’m just highly motivated to do nothing.",
                   "Don’t worry if plan A fails, there are 25 more letters in the alphabet.",
                   "The first five days after the weekend are the toughest.",
                   "Do you remember when I asked you to give me your opinion? That’s right, me neither.",
                   "Whenever I’m bored, I go to my favorite place: The fridge."
                   ]

print()
#Create a "while True" loop to print out casual jokes from the "jokes_sentences" list, using the "choice" function
#from the random module. I set also a second "while True" loop to give the choice to the user to get new jokes in case
#wants it or not.
while True:
    enter = input("PRESS ENTER TO GENERATE A CASUAL JOKE!")
    print("\n" + random.choice(jokes_sentences))
    while True:
        selection = input("\nENTER 'Y' TO GENERATE A NEW CASUAL JOKE OR ENTER ANY CHARACTER TO EXIT: ").lower()
        if selection == "y":
            print("\n" + random.choice(jokes_sentences))
        else:
            print("\nTHANK YOU, SEE YOU NEXT TIME!")
            exit()
