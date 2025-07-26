from game_data import data
import random
import art
import os
print("game.py is being imported")

def logo():
    """print the logo and introduction"""
    print(art.logo)
    print("Welcome to the Higher Or Lower game. \n"
          "Here we compare who has more instagram follower.😎")


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

#def a function to compare the followers
def compare_follower(account1, account2, user_guess):
      account_followers1=account1["follower_count"]
      account_followers2 = account2["follower_count"]
      if account_followers1>account_followers2:
            return user_guess=="a"
      elif account_followers1<account_followers2:
            return user_guess=="b"
      else:
            return "bonus"
      

def get_new_account(exclude=None):
    """keeps the options different by excluding option A."""
    new_account = random.choice(data)
    while new_account == exclude:
        new_account = random.choice(data)
    return new_account

def get_user_input():
    """Gets user input and checks for valid entries"""
    guess = str(input("Who has more followers? What's your take? \n"
                      "Type 'a' or 'b': ")).lower().strip().replace(" ", "")

    if guess == "a" or guess == "b":
        return guess  # return actual input

    else:
        print("Please enter valid input. Type 'a' or 'b'.")


def game_logic():
    playing = True  
    while playing:
      score = 0
      game_over = False
      option_b = random.choice(data)
      logo()
      while not game_over:
            # print two random entries from the data for comparison
            option_a = option_b
            option_b = get_new_account(exclude=option_a)

            print(f"\nOPTION_A: {format_data(option_a)}")
            print(art.vs)
            print(f"OPTION_B: {format_data(option_b)}\n")

            
            user_input=get_user_input()

            if user_input:
                  # compare the entries and update score
                  is_correct = compare_follower(option_a, option_b, user_input)
                  if is_correct:
                        score += 1
                        print(f"The answer was correct.✅ You get a point!👍 Your score is {score}.")
                  elif is_correct=="bonus":
                        score += 1
                        print("Both accounts have the same number of followers. \n"
                              f"You get a Bonus Score!😁 Your score is {score}.")
                  else:
                        print(f"Oops! You Lose.😭 Your score is {score} ")
                        game_over=True
                        
            else:
                  continue
      # Ask after the game is over
      rerun = input("Do you want to play again? Type 'Yes' or 'No': ").lower().strip()
      if rerun != "yes":
            playing = False
            print("THANK YOU FOR PLAYING. SEE YOU SOON! 🤗")
      else:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen



if __name__ == "__main__":
    print("Running game.py directly")
    game_logic()






