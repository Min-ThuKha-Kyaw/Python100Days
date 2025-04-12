def rollercoaster():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? : "))
    if height >= 120:
        print("You can ride the rollercoaster!")
        price = 0
        
        age = int(input("What is your age? : "))
        if age < 12:
            price += 5
            print("Child tickets are $5.")
        elif age <= 18:
            price += 7
            print("Youth tickets are $7.")
        elif age >= 45 and age <= 55:
            print("Have a free ride!!!")
        else:
            price += 12
            print("Adult tickets are $12.")
        want_photo = input("Do you want a photo taken? Y or N >>  ")
        if want_photo == "Y":
            price += 3
         
        print(f"\nYour ticket price will be : ${price}.")
            
    else:
        print("You can't ride the rollercoaster, You need to grow taller")


def ODDorEVEN():
    number = int(input("Which number do you want to check? : "))
    if number % 2 == 0:
        print(f"Your number : {number} is an Even.")
    else:
        print(f"Your number : {number} is an Odd.")


def BMI():
    weight = float(input("Please enter your weight in KG : "))
    height = float(input("Plesas enter your height in m : "))
    bmi = weight / height ** 2
    if bmi < 18.5:
        print(f"Your BMI is {round(bmi,1)}, you are underweight!")
    elif bmi <25:
        print(f"Your BMI is {round(bmi,1)}, you have a normal weight!")
    elif bmi <30:
        print(f"Your BMI is {round(bmi,1)}, you are overweight!")
    elif bmi <35:
        print(f"Your BMI is {round(bmi,1)}, you are obese!!")
    else:
        print(f"Your BMI is {round(bmi,1)}, you are clinically obese!!!")


def leapyear():
    year = int(input("Which year you want to check? : "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The year {year} is a leap year.")
            else:
                print(f"The year {year} is not a leap year.")
        else:
            print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")


def pizzaOrder():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L >>  ")
    add_pepperoni = input("Do you want pepperoni? Y or N >>  ")
    extra_cheese = input("Do you want extra cheese? Y or N >>  ")
    bill = 0
    
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    else:
        print("Please enter valid keywords!!!")
    
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
        
    if extra_cheese == "Y":
        bill += 1
        
    print(f"Your Final Bill will be ${bill}")
        

def loveCalculator():
    print("Welcome to the Love Calculator!")
    name1 = input("Please enter your name >>>  ")
    name2 = input("Please enter their name >>>  ")
    
    combine_name = name1 + name2
    uppercase_name = combine_name.upper()
    
    T = uppercase_name.count("T")
    R = uppercase_name.count("R")
    U = uppercase_name.count("U")
    E = uppercase_name.count("E") 
    TRUE = str(T + R + U + E)
    
    L = uppercase_name.count("L")
    O = uppercase_name.count("O")
    V = uppercase_name.count("V")
    E = uppercase_name.count("E")
    LOVE = str(L + O + V + E)
    
    score = int(TRUE + LOVE)
    
    if score < 10 or score > 90 :
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

def main():
#     rollercoaster()
#     ODDorEVEN()
#     BMI()
#     leapyear()
#     pizzaOrder()
    loveCalculator()


main()