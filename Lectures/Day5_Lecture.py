def looping():
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
        print(fruit + "Pie")
    print(fruits)
    
    for k in range(1, 10,2):
        print(k)
    
def averageHeight():
    student_heights = input("Please enter a list of student heights >>>  ").split()
    total_height = 0
    total_number = 0 
    for n in range(0, len(student_heights)):
        heights = int(student_heights[n])
        total_height += heights
        total_number += 1
    average_height = round(total_height / total_number)        
    print(student_heights)
    print(f"The average height of the students is {average_height}")
    
def averageHeight1():
    stu_heights = input("Please enter a list of student heights >>> ").split()
    for i in range(0, len(stu_heights)):
        stu_heights[i] = int(stu_heights[i])
    average_height = sum(stu_heights) / len(stu_heights)
    print(average_height)
    
    
def scoreCheck():
    student_scores = input("Enter a list of student scores >>>  ").split()
    for h in range(0, len(student_scores)):
        student_scores[h] = int(student_scores[h])
    
    highest_score = 0 
    for score in student_scores:
        if score > highest_score:
            highest_score = score
    print(f"The Highest score in the class is : {highest_score}.")
        

def SumofEven():
    result = 0
    for even in range(1,101):
        if even % 2 == 0:
            result += even
    print(result)
        
        
def fizzBuzz():
    for number in range(1, 101):
        if number % 15 == 0 :
            print("FizzBuzz")
        elif number % 3 == 0 :
            print("Fizz")
        elif number % 5 == 0 :
            print("Buzz")
        else:
            print(number)
        
def main():
#     looping()
#     averageHeight1()
#     averageHeight()
#     scoreCheck()
#     SumofEven()
    fizzBuzz()
    
main()