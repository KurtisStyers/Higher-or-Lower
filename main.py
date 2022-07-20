import art
import game_data

import random
import os


# Function for picking random person
def get_person(prev_person):
    new_person = random.choice(game_data.data)
    while new_person["name"] == prev_person["name"]:
        new_person = random.choice(game_data.data)

    return new_person


# Function for comparing followers
def get_results(usr_choice, person_1, person_2):
    if usr_choice == 'a':
        if person_1['follower_count'] > person_2["follower_count"]:
            return False
        else:
            return True
    elif usr_choice == 'b':
        if person_2['follower_count'] > person_1["follower_count"]:
            return False
        else:
            return True
    else:
        return True


score = 0
finished = False
person_b = random.choice(game_data.data)
person_a = get_person(person_b)

while not finished:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    finished = get_results(choice, person_a, person_b)

    if not finished:
        score += 1
        person_a = person_b
        person_b = get_person(person_a)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)
        print(f"Sorry that's wrong. Final score: {score}.")
