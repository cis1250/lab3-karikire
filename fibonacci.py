#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
  userInput = input("How many terms of the fibonacci sequence do you want?: ")

  if not userInput.isdigit():
   print("Please enter a prositive whole number integer")
   continue
    
  k=int(userInput)
  
  if (k <=0):
    print("Please enter a positive whole number integer")
    continue


  break

a=0
b=1
for i in range(k):
  print(a, end=" ")
  a, b=b, a+b
print()
