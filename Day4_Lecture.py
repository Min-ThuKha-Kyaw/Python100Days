import random

def randoming():
    random_integer = random.randint(1,10)
    print(random_integer)
    
    random_float = random.random() * 5
    print(random_float)
    
    random_float = random.uniform(0,5)
    print(random_float)
    
def TailOrHead():
    print("Welcome to the random coin flip")
    result = random.randint(1,2)
    print(result)
    if result == 1 :
        print("Heads")
    else:
        print("Tails")
  
  
def pythonlist():
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virgina", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennnessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michingan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakato", "South Dakato", "Montana", "Washington", "Idoha", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
    print(states_of_america[-1])
    

def payingbill():
    names_string = input("Give me everybody's names, seperated by a comma >>>  ")
    names = names_string.split(",")    
    result = random.randint(0, len(names)-1)
    print(result)
    person = names[result]
    print(f"{person} is going to buy the meal today")
    
    
def food():
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#     dirty_dozen = fruits+ vegetables
    dirty_dozen = [fruits , vegetables]
    print(dirty_dozen)
    
   
def treasureMap():
    row1 = ["🌁","🌁","🌁"]
    row2 = ["🌁","🌁","🌁"]
    row3 = ["🌁","🌁","🌁"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure >>>  ")
    
    horizonal = int(position[0])
    vertical = int(position[1])
    
    map[vertical-1][horizonal-1] = "X"
    print(f"\n{row1}\n{row2}\n{row3}")

    
     
    

def main():
#     randoming()
#     TailOrHead()
#     pythonlist()
#     payingbill()
#     food()
    treasureMap()
    
    
main()

