# Core:
# * Write a program that prints the numbers from 1 to 100.
# * For multiples of three print "Fizz" instead of the number
# * For the multiples of five print "Buzz" instead of the number
# * For numbers which are multiples of both three and five print "FizzBuzz".
#
# Extra:
# * make a new fizzbuzz file and make it functional
# * make it, so we can decide which numbers to substitute for fizz and buzz using functions
#

range_of_nums = int(input("Please enter range of numbers to test: "))
fizz_num = int(input("Input fizz number: "))
buzz_num = int(input("Input buzz number: "))

for num in range(range_of_nums):
    if (num % fizz_num) == 0 and (num % buzz_num) == 0:
        print("FizzBuzz")
    elif (num % fizz_num) == 0:
        print("Fizz")
    elif (num % buzz_num) == 0:
        print("Buzz")
    else:
        print(num)
