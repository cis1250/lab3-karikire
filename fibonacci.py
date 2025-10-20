#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.1

#Here I get the user input and make sure its a whole number
def get_num_terms():
    while True:
        user_input = input("How many terms of the Fibonacci sequence do you want?: ")
        if not user_input.isdigit():
            print("Please enter a positive whole number integer.")
            continue
        k = int(user_input)
        if k <= 0:
            print("Please enter a positive whole number integer.")
            continue
        return k

#The same code from before, to generate the fibonacci sequence
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

#Makes each number a string because if it's integer the code will crash
def print_sequence(seq):
    print("Fibonacci sequence:")
    print(" ".join(map(str, seq)))

#The part that runs the actual program
def main():
    num_terms = get_num_terms()
    fib_seq = generate_fibonacci(num_terms)
    print_sequence(fib_seq)

if __name__ == "__main__":
    main()

