import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*','+']

print("Welcome to the PyPassword Generator!!")
nr_letters = int(input("How many letters would you like in your password >>>  "))
nr_symbols = int(input("How many symbols would you like in your password >>>  "))
nr_numbers = int(input("How many numbers would you like in your password >>>  "))

random_choice = []
for letter in range(nr_letters):
    random_choice.append(random.choice(letters))


for symbol in range(nr_symbols):
    random_choice.append(random.choice(symbols))
    

for number in range(nr_numbers):
    random_choice.append(random.choice(numbers))
    
print(random_choice)
random.shuffle(random_choice)
print(random_choice)

result = ""
for char in random_choice:
    result += char
print(f"Your password should be : {result}")
