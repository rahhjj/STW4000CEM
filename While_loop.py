

# question no 1
# Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, print "You are an adult." For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."

user_input = False

while not user_input:
    keyword = input("Enter your age or type 'stop' to exit: ").lower()

    if keyword == 'stop':
        print("Program stopped.")
        user_input = True
        continue

    if keyword.isdigit():
        age = int(keyword)
        
        if age < 18:
            print("You are a minor.")
        elif 18 <= age <= 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    else:
        print("Invalid input. Please enter a valid age or type 'stop' to exit.")

# question no 2
# Write a Python program that simulates waiting for a 
# specific vehicle, such as a "bus". The program should 
# repeatedly prompt the user to input the name of a vehicle. 
# If the input is not "bus", the program should print 
# "waiting" and continue. Once the user inputs "bus", the 
# program should print "finally the wait is over" and terminate the loop

bus = False
while bus == False:
    vehicle_name = input("Enter the name of vehicle: ").lower()
    if vehicle_name != 'bus':
        print('waiting')
        continue
    else:
        print('finally the wait is over.')
        bus = True

# question no 3
# Write a Python program that continuously prompts the user 
# to input a fruit name. If the input is "apple," the program 
# should print "You got it!" and stop. Otherwise, it should 
# display "Try again" and continue.   
    
apple = False

while apple == False:
    fruit_name = input("Enter the name of a fruit: ").lower()
    
    if fruit_name == 'apple':
        print("You got it!")
        apple = True
    else:
        print("Try again")

# question no 4
# Create a Python program that asks the user to guess the password.
# The program should keep asking until the user enters "open sesame."
# For each incorrect guess, print "Wrong password, try again." 
# When the correct password is entered, print "Access granted!"

guess_passowrd = False
while guess_passowrd == False:
    password = input("Enter the correct password: ").lower()
    if password == 'open sesame':
        print("Access Granted!")
        guess_passowrd = True
    else:
        print("Try again!")

# question no 5
# Write a Python program that keeps asking the user to enter a 
# day of the week. If the input is not "Sunday," print "It's not 
# the weekend yet." The loop should break and print "Enjoy your weekend!"
# when the input is "Sunday."

sunday = False

while sunday == False:
    day = input("Enter the day of week: ").lower()
    
    if day == 'sunday':
        print("Enjoy your weekend!")
        sunday = True
    else:
        print("It's not weekend yet!")

# quesiton no 6
# Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.

import random

random_number = random.randint(1, 10)
attempts = 0
successful_guess = False

print("Guess the number (between 1 and 10):")

while successful_guess == False:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess < random_number:
        print("Guess higher!")
    elif guess > random_number:
        print("Guess lower!")
    else:
        print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")

# question no 7
# Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit. If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."    

attempts = 3
error = False
i = 0
while error == False:
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    if user_id == "admin" and password == "admin123":
        print("You are logged in successfully")
        break
    else:
        i = i + 1
        if i != attempts:
            print(f"You have {attempts-i} attempts left.")
            continue
        else:
            error = True
            print("You are blocked!") 

# question no 8
# Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"

import random
a = random.randint(1, 30)
b = random.randint(1, 30)
product = a * b
print(f"{a}, {b}, product is {product}")
guess = False

while guess == False:
    user_guess = int(input("Enter your guess: "))
    
    if user_guess == product:
        print("Correct")
        cont = input("enter your response: ").lower()
        if cont == 'yes':
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            product = a * b
            print(f"{a}, {b}, product is {product}")
            continue
        else:
            break
    else:
        guess = True
        print("Incorrect")
        print(f"product is {product}")
        print(f"your guess is {user_guess}")

# question no 9
# Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
# "The number is not prime." Continue prompting the user until they enter "exit."

while True:
    user_input = input("Enter a number (or type 'exit' to stop): ").lower()
    
    if user_input == "exit":
        print("Program stopped.")
        break

    if user_input.isdigit():
        num = int(user_input)
        if num < 2:
            print("The number is not prime.")
        else:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("The number is prime.")
            else:
                print("The number is not prime.")
    else:
        print("Invalid input. Please enter a valid number or 'exit'.")

# question no 10
# Write a Python program that asks the user to guess a pre-defined secret
# word (e.g., "python"). Provide feedback like "Incorrect, try again" if the 
# guess is wrong. When the user guesses correctly, print "Congratulations, you
# guessed the word!" Allow the user to exit the program by typing "quit."

secret_word = "python"
word_guessed = False
while word_guessed == False:
    user_input = input("Guess the secret word (or type 'quit' to exit): ").lower()

    if user_input == "quit":
        print("Program exited.")
        break
    elif user_input == secret_word:
        print("Congratulations, you guessed the word!")
        word_guessed = True
    else:
        print("Incorrect, try again.")
  
# question no 11
# Write a Python program that prompts the user to repeatedly enter a name. 
# If the user enters the phrase "good luck," the program keeps track of how many 
# times the phrase has been entered. When the phrase has been entered three times, 
# the program should display a message stating "You typed good luck three times." 
# For each entry of "good luck" before the third occurrence, display the message 
# "You typed the same word [count] times." Continue this process until the phrase 
# has been entered three times.

count = 0

while count < 3:
    user_input = input("Enter a name or a phrase: ").lower()

    if user_input == "good luck":
        count = count + 1
        if count < 3:
            print(f"You typed the same word {count} time(s).")
        else:
            print("You typed good luck three times.")
    else:
        print("Keep going!")

    