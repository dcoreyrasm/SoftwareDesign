#Program prompts user to enter an integer between 5 and 10 (inclusive) until
#they do so correctly.

number = input("Enter an integer between 5 and 10 (inclusive): ")

while number >10 or number < 5:
    print "Invalid input!",
    number = input("Enter an integer between 5 and 10 (inclusive): ") 

print ("Thank-you!")