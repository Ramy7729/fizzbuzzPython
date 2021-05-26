def fizzbuzz(test_number):
  # Conditional that prints FizzBuzz if a number is divisble by both 3 and 5.
  # The modulo is used to return the remainder of 0 for it to be divisble by a number.
  if(test_number % 3 == 0 and test_number % 5 == 0):
    print("FizzBuzz")
  # Conditional that prints Fizz if a number is divisble by 3.
  elif(test_number % 3 == 0):
    print("Fizz")
  # Conditional that prints Buzz if a number is divisble by 5.
  elif(test_number % 5 == 0):
    print("Buzz")
# This is our list of numbers    
numbers = [3, 5, 10, 15, 20, 21, 23, 24, 25, 30, 37, 41, 45, 50, 51, 77, 97]
# This for loop iterates through the list
# The fizzbuzz function is called and takes in a number from list.
for number in numbers:
  fizzbuzz(number)
