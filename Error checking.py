# Error checking
# GG
# 14 October 2026

# Code that tests whether a valid input was given (v1)
'''done = True # Boolean variables set to True
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

    print(f"The number you entered is {num}")'''

# Using a try and except method to check for valid input (V2)
# Use try and except method to catch errors
done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \n")

print(f"The number you entered is {num}.")