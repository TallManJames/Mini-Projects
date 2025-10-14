
#this project will be to have a number guessing game, 3 difficulties, but you have attempts to guess the number, there will be a leaderboard, etc

import random , time

class Game:
    def __init__(self):
        self.easyLeaderboard = []
        self.mediumLeaderboard = []
        self.hardLeaderboard = []
    
    def play(self):
        print("Welcome to the Number Guessing Game!")
        name = input("What is your name?: ").capitalize()

        #(number range, max attempts)
        difficulties = {
            "easy": (50, 10),
            "medium": (100, 15),
            "hard": (200, 20)
        }

        #showcase difficulties
        print("\nPlease select from the list which difficulty you would like to play:")
        for key, (max_num, max_attempts) in difficulties.items():
            print(f"{key.capitalize()} mode: Pick a number from 1 to {max_num}, with {max_attempts} attempts.")
        time.sleep(3)
        #select difficulty
        while True:
            diff_choice = input("Which difficulty you would like: Easy, Medium, or Hard\n").lower()
                
            if diff_choice == "easy":
                
                break
            elif diff_choice == "medium":
                
                break
            elif diff_choice == 'hard':
                
                break
            else:
                print("Error, please select a difficulty from the list.")
                
            

        #print(f"Test: your name is {name} and the difficulty you chose is {diff_choice} which has {___} attempts for guessing between 1 to {___}")

while True:
    Game.play(self="")
    break