import random
from art import logo
from art import vs
from game_data import data
should_continue = True
score = 0

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"

def check_answers(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
print(logo)
account_b = random.choice(data)
while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answers(guess,a_follower_count,b_follower_count)

    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue=False