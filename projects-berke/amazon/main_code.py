
from amazon_1_question import SegregateArray
from amazon_2_question import AscendingOrder
from amazon_7_question import FizzBuzz



def ask_continue_solve_problem():
    ''' ask if user wants to continue solving problem'''
    global is_on
    continue_question = input("Do you want to continue with other problems? Y or N: ")
    if continue_question == "Y":
        is_on = True
    else:
        print("Thank you for solving the problems. Have a nice day!")
        is_on = False

is_on =True

while is_on == True:
    question_number = input("Which question would you like to solve: \n 1)Q1\n 2)Q2\n 3)Q3\n 4)Q4\n 5)Q5\n 6)Q6\n 7)Q7\n")

    if question_number == "1":
        numbers = list(map(int, input("Enter numbers for segregate an array of random numbers by EVEN or ODD value: (ex: 1 3 9 2 .. ..): \n").split()))
        segrated_numbers_array = SegregateArray.segregate_array(numbers)
        print(segrated_numbers_array)

    elif question_number == "2":
        numbers = list(map(int, input("Enter multiple values for ascending numbers:(ex: 1 3 9 2 .. ..): \n").split()))
        print(AscendingOrder.bubble_sort(numbers))

    elif question_number == "7":
        numbers = int(input("Enter number for FizzBuzz Game: \n"))
        FizzBuzz.fizz_buzz_game(numbers)

    else:
        exit()

    ask_continue_solve_problem()























