'''Write a program that prints out the integer numbers from 1 to 100.
- If the number is divisible by three, print "Fizz" instead of the number.
- If the number is divisible by 5, print "Buzz" instead of the number.
- If the number is divisible by 3 and 5 then do not print that number but skip it.'''


class FizzBuzz:
    def fizz_buzz_game(number):

        for i in range(1,number+1):
            if i % 3 == 0 and i % 5 == 0:
                continue
            elif i % 3 == 0:
                return ("Fizz")
            elif i % 5 == 0:
                return("Buzz")
            else:
                return(i)






