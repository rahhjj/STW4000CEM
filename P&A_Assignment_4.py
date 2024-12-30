
# question no 1
# print "softwarica" 10 times
for i in range(10):
    print("Softwarica")

# question no 2
# sum of a list
Sample_list = [8, 2, 3, 0, 7] 
sum = 0
length = len(Sample_list)
for x in range(length):
    sum = sum + Sample_list[x]
print(sum)

# question no 3
# print each character using indexing
character = input("Enter the character: ")
for x in range (len(character)):
    print(f"{character[x]} is at index {x}")
 
# question no 4
# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
sample_list = [1, "a", "c", 2, 3, 4]
for x in sample_list:
    if isinstance(x,int): # used to check if a number is in particular type
        print(x)
  
# question no 5
# multiplication of a each element. given list=[4,5,3,2]
Sample_list = [4,5,3,2]
product = 1
length = len(Sample_list)
for x in range(length):
    product = product * Sample_list[x]
print(product)  

# question no 6
# multiplication table of given number
num = int(input("Enter your number: "))
for i in range(11):
    print(num, "*", i, "=", (num * i))
    
# question no 7
# reverse a list
sample_list = [1,2,3,4,5] 
reversed_list = []
for numbers in sample_list:
    reversed_list.insert(0, numbers)    # insert function is used to insert elements
print(reversed_list)                    # taking two arguements of index and number to be inserted
 
# question no 8
# given list is [1,2,3,4] but expected output in new list [2,3,4,5]
sample_list = [1,2,3,4]
new_list = []
for x in sample_list:
    new_list.append(x + 1) # append is used to update a list
print(new_list)
 
# question no 9
# Given list is list=[1,2,3,4] but print 1 and 4 only
list = [1,2,3,4]
for x in list:
    if x == 1 or x == 4:
        print(x)
        continue

# question no 10
# Given list is list=[1,2,3,4] but print 1 2 and 4 only    
list = [1,2,3,4]
for x in list:
    if x == 1 or x == 2 or x == 4:
        print(x)
        continue
    
# question no 11
# Given list is [1,2,3,4] but expected output is [1,"a",2,4]    
list = [1,2,3,4]
for x in range(4):
    if list[x] == 2:
        list[x] = 'a'
        print(list)

# question no 12
# Given list is [1,2,3,4,5] separate the elements into odd and even categories.
list = [1,2,3,4,5]
odd_list = []
even_list = []
for x in list:
    if x % 2 == 0:
        even_list.insert(0, x)
    else:
        odd_list.insert(0, x)
print(odd_list)
print(even_list)
 
# question no 13
# Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
sample_list = [1,2,3,"d",4,5,"a"]
integer = []
string = []
for x in sample_list:
    if isinstance(x,int): # used to check if a number is in particular type
        integer.insert(0, x)  
    elif isinstance(x, str):
        string.insert(0, x)   
    else:
        print("Not a valid datatype.") 
print(integer)
print(string)
 
# question no 14
# Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists
sample_list = [1,2,3,4,"a","b"]
integer = []
string = []
for x in sample_list:
    if isinstance(x,int): # used to check if a number is in particular type
        integer.append(x) 
    elif isinstance(x, str):
        string.append(x)   
    else:
        print("Not a valid datatype.") 
print(integer)
print(string)

# question no 15
# Python program that accepts a string and calculate the number of digits and letters and space
character = input("Enter the sentence: ")

digits = 0
alphabets = 0
spaces = 0

for x in character:
    if x.isdigit():
        digits += 1
    elif x.isalpha():
        alphabets += 1
    elif x.isspace():
        spaces += 1

print(f"Input: {character}")
print(f"Number of letters: {alphabets}")
print(f"Number of digits: {digits}")
print(f"Number of spaces: {spaces}")

# question no 16
# Python program to check the validity of username and password input by users
attempts = 3
for i in range(1, 4):
    user_id = input("Enter your user ID: ")
    password = input("Enter your password: ")
    if user_id == "admin" and password == "admin123":
        print("You are logged in successfully")
        break
    else:
        if i != attempts:
            print(f"You have {attempts-i} attempts left.")
            continue
        else:
            print("You are blocked!")

# question no 17
# program to print the given number is odd or even
user_input = int(input("enter the number to be checked"))

remainder = user_input % 2

if remainder == 0:
    print("user input is an even number")
else:
    print("user input is an odd number")

# question no 18
# factorial of a given number
fact = 1
num = int(input("Enter a number: "))
for x in range(num, 0, -1):
    fact = fact * x
print(fact)

# question no 19
# Print multiplication table of  1,2,3,4,5,6,7,8
num = int(input("Enter your number (1,2,3...9): "))
for i in range(11):
    print(num, "*", i, "=", (num * i))

# question no 20
# Given list is lst=[1,2,3,4] but print 1 and 2 only
list = [1,2,3,4]
for x in list:
    if x == 1 or x == 2:
        print(x)
        continue


# question no 21
# Python program to calculate the sum of all the odd numbers within the given range
odd_sum = 0
final_range = int(input("Enter the range: "))
for x in range(final_range):
    if x % 2 != 0:
        odd_sum = odd_sum + x
print(odd_sum)

# question no 22
# Python program to calculate the sum of all the even numbers within the given range.
even_sum = 0
final_range = int(input("Enter the range: "))
for x in range(final_range):
    if x %2 == 0:
        even_sum = even_sum + x
print(even_sum)

# question no 23
# Python program to count the space of a given string
blank_space = 0
character = input("Enter your sentence: ")
for x in range(len(character)):
    if character[x] == " ":
        blank_space = blank_space + 1
print(blank_space)

# question no 24
# given list is [1,2,3,4] but expected output is [1,8,27,64]
sample_list = [1,2,3,4]
new_list = []
for x in sample_list:
    new_list.append(x**3) # append is used to update a list
print(new_list)

# question no 25
# reverse of a string a="programming"
a="programming"
for i in range(-1, -(len(a)+1), -1):
    print(a[i])

# question no 26
# Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for x in range(50):
    if x <= 7:
        print(x)
    else:
        break

# question no 27
# Write a for loop that iterates through a string and prints every letter
a = input("Enter the string: ")
for x in range(len(a)):
    print(a[x])

# question no 28
# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". 
# Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a = ["ram", "shyam", 1, 2]

for item in a:
    if isinstance(item, str):  # Check if the item is a string
        print(f"Hello!{item}")

# question no 29
# Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"]
# expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']

a = ["ram", "shyam", 1, 2]
result = []

for item in a:
    result.append(f"Dr.{item}")

print(result)

# question no 30
# Write a for loop which appends the square of each number to the new list.

a = [1, 2, 3, 4, 5] 
squared_numbers = []

for num in a:
    squared_numbers.append(num ** 2)  # Append the square of the number

print(squared_numbers)

# question no 31
# Write a for loop using an if statement, that appends each number to the new list if it's positive.
# given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

list = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = []

for num in list:
    if num > 0:  # Check if the number is positive
        positive_numbers.append(num)

print(positive_numbers)

# question no 32
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
# given list=[0,1,2,3,4,5,6]
lst = [0, 1, 2, 3, 4, 5, 6]

for num in lst:
    if num != 3 and num != 6:  # Exclude 3 and 6
        print(num)

# question no 33
# Write a for loop which appends the type of each element in the first list to the second list
first_list = [1, "hello", 3.14, True, [1, 2, 3], {"key": "value"}]
second_list = []

for element in first_list:
    second_list.append(type(element))  # Append the type of the element

print(second_list)

# question no 34
# Use else block to display a message “Done” after successful execution of for loop.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Done")

# question no 35
# Write a for loop statement to print the following series: 105 98 -------7
for x in range(105, 0, -7):
    print(x)

# question no 36
# removal bad characters from the given string. 
# Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython

bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"

# Remove bad characters
for char in bad_chars:
    string = string.replace(char, "")  # Replace each bad character with an empty string

# Remove spaces
string = string.replace(" ", "")

print(string)

# question no 37
# Python program to count the number of even and odd numbers from a series of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example series of numbers
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else: 
        odd_count = odd_count+ 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

# question no 38
# Write a for loop to find the sum of all multiples of 3 or 5 below a given number range from 3 to 99.
total_sum = 0

for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0: 
        total_sum = total_sum + num  

print(f"The sum of all multiples of 3 or 5 below 100 is: {total_sum}")

# question no 39
# Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.

even_sum = 0
odd_sum = 0

for num in range(1, 101):
    if num % 2 == 0:  
        even_sum = even_sum + num 
    else:
        odd_sum = odd_sum + num 

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

# question no 40
# program to check given number is palindrome or not

number = int(input("Enter a number: "))

original_number = number
reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = reversed_number * 10 + remainder
    number = number // 10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")

# question no 41
# program to check given number is armstrong or not Input number from the user

number = int(input("Enter a number: "))
original_number = number
sum_of_cubes = 0

num_digits = len(str(number))

while number > 0:
    digit = number % 10
    sum_of_cubes += digit ** num_digits
    number = number // 10
if original_number == sum_of_cubes:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")

# question no 42
# Write a for loop that removes all vowels (a, e, i, o, u) from a string

input_string = input("Enter a string: ")
result_string = ""

for char in input_string:
    if char.lower() not in 'aeiou':
        result_string = result_string + char

print("String after removing vowels:", result_string)

# question no 43
# python program to check a number is perfect number

number = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors = sum_of_divisors + i

if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

# question no 44
# You have two lists of numbers, and you need to find out which numbers appear in both lists.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common_numbers = []

for num in list1:
    if num in list2:
        common_numbers.append(num)

print("Common numbers:", common_numbers)

# question no 45
#  Write a program to determine whether a given number is a prime number.

number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
