
class FizzBuzz:
    def fizz_buzz_game(number):
        '''Write a program that prints out the integer numbers from 1 to 100.
        - If the number is divisible by three, print "Fizz" instead of the number.
        - If the number is divisible by 5, print "Buzz" instead of the number.
        - If the number is divisible by 3 and 5 then do not print that number but skip it.'''

        for i in range(1,number+1):
            if i % 3 == 0 and i % 5 == 0:
                continue
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print (i)






