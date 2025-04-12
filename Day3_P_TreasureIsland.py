print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
direction = input("Your are at a cross road. There are 2 ways? Type 'Left' or 'Right' >>>  ").upper()
if direction[0] == "L":
    options = input("You have arrived a coastal area. Type 'Swin' or 'Wait' >>>  ").upper()
    if options[0] == "W":
        doors = input("You have arrived a castle. There are 3 doors. Type 'Red' , 'Blue' or 'Yellow' >>>  ").upper()
        if doors[0] == "Y":
            print("Yay!!! You have entered the room full with gold. You found the treasure.")
        elif doors[0] == "B":
            print("You drop into the sea. Game over!")
        elif doors[0] == "R":
            print("You have entered the room of fire. Game over!")
        else:
            print("Please type the valid keywords.")
    elif options[0] == "S":
        print("You drown at the half way. Game over!")
    else:
        print("Please type the valid keywords.")
elif direction[0] == "R":
    print("Car crashed toward you. Game over!")
else:
    print("Please enter the valid keywords.")
    
