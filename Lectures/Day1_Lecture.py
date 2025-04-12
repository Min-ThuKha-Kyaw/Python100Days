def printing():
    print("Day 1 - Python Print Function")
    print("The function is declared like this:")
    print("print('what to print')")
    print("Hello World!\nHello World!\nHello World!")
        
def debugging():
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")
                
def string_manipulation():
    print("Hello" + "      Angela")
    print("Hello "+ input("what is your name? :"))
    print(f"Welcome, {input('What is Your Name? : ')} : {int(input('What is Your Age? : '))} ")
        
def inputting():
    name = input("What is your name ? : ")
    age = int(input("Enter your age : "))
    print(name , age)
    print("Welcome " + input("What's Your Name? : "))
    
def inputexe():
    print(len(input("What's your name? \n")))

def variable():
    a = input("a : ")
    b = input("b : ")
    c = a
    a = b
    b = c   
    print("a = "+ a)
    print("b = "+ b)
    

def main():
#     printing()
#     string_manipulation()
#     debugging()
#     inputting()
#     inputexe()
    variable()
    
main()