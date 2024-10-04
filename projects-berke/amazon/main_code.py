import random

from amazon_2 import AscendingOrder
from amazon_7 import FizzBuzz


question_number = input("Which question would you like to solve: ")

is_on =True
while is_on == True:

    if question_number == "2":

        numbers = list(map(int, input("Enter multiple values: ").split()))
        print(AscendingOrder.bubble_sort(numbers))

    elif question_number == "7":
        number = int(input("Enter number: "))
        FizzBuzz.fizz_buzz_game(number)


continue_question = input("Do you want to continue to solve problem? Y or N: ")



















