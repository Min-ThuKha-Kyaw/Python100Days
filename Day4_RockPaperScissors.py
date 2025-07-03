import random 

def rockpaperscissors():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    
    paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
    
    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    list1 = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper' or 2 for 'Scissors' >>>  "))
    if user_choice >= 3 or user_choice < 0:
        print("Please enter the valid number")
    else:
        print(list1[user_choice])

        random_number = random.randint(0,2)
        print("Computer chose : ")
        print(list1[random_number])
        

        if user_choice == 0 and random_number == 1:
            print("You lose")
        elif user_choice == 1 and random_number == 2:
            print("You lose")
        elif user_choice == 2 and random_number == 0:
            print("You lose")
        elif user_choice == 0 and random_number == 2:
            print("You win")
        elif user_choice == 2 and random_number == 1:
            print("You win")
        elif user_choice == 1 and random_number == 0:
            print("You win")
        
        else:
            print("Draw")
    
def main():
    rockpaperscissors()
    
main()
