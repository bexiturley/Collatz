# The number we will perfrom the Collatz operations on.

n = int (input ( "Enter a number: " ))

# Keep looping until we reach 1.
# Note: This assumes the Collatz conjecture is true.

while n !=1:
    # Print the current value of n.
    print (n)
    # Check if n is even.
    if n % 2 == 0:
        # If n is even, divide it by 2.
        n = n // 2
    else:
        # If n is odd, multiply by three and add 1.
      n = (3 * n) + 1

# Finally, print the 1.
print (n)


