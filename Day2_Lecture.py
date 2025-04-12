def primitive_dataType():
    print("Hello" [0])
    number = 123_456_789
    print(type(number))
    print(number)
    
def typeError():
    num_char = len(input("What is your name? : "))
    print("Your name has " + str(num_char) + " characters.")
    
def addingDigit():
    two_digit_number = input("Type a two digit number: ")
    result = int(two_digit_number[0]) + int(two_digit_number[1])
    print(result)
    
    
def bmi():
    height = input("Enter your Height in m : ")
    weight = input("Enter your Weight in kg : ") 
    bmi = int(float(weight) / float(height) ** 2)
    print(bmi)
    
def lifeinWeek():
    age = input("What is your current age? : ")
    left = 90 - int(age)
    dayleft = left * 365
    weekleft = left * 52
    monthleft = left * 12
    print(f"You have {dayleft} days, {weekleft} weeks, and {monthleft} months left.") 
    
    
    
def main():
#     primitive_dataType()
#     typeError()
#     addingDigit()
#     bmi()
    lifeinWeek()
    
    
main()