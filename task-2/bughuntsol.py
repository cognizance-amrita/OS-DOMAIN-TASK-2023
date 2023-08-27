def calc_average(numbers):
    total = 0
    count = 0 #To properly initialize the count variable "Count == 0"
    for num in numbers:
        total += num
        count += 1
    avg = total / count #It should be count instead of coun
    return avg


# Test the function
nums = [10, 20, 30, 40, 50]
result = calc_average(nums)
print("Average:", result)  # It should be result instead of resul
# Check if the average is even or odd
if result % 2 == 0:  #Use == for comparison instea of =
    print("The average is even")
else:
    print("The average is odd")

# Generate a list of squares
squares = [num ** 2 for num in nums] #Missing a closing square bracket
print("Squares:", squares)

# Find the maximum square
max_square = max(squares)
print("Maximum square:", max_square) #It should be 'max_square' instead of 'max_sqaur'

# Search for a specific square
target_square = 900
if  target_square in squares:  #if statement is missing a colon and also identation
  print("Target square found at index:", squares.index(target_square))
else:
  print("Target square not found")

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

# Remove duplicates from the list
unique_list = list(set(combined_list))
print("Unique list:", unique_list)

# Create a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Person's name:", person['name'])
print("Person's gender:", person.get('gender', 'Unknown'))

# Update the person's age
person['age'] = 26
print("Updated age:", person['age'])

# Add a new key-value pair
person['job'] = 'Engineer'

# Delete the city key
del person["city"]

# Print all key-value pairs in the dictionary
for key, value in person.items(): #missing paranthesis after items
    print(f"{key}: {value}") #use an f-string to print the key and value

    # Check if person is from London
if person['city'] == 'London': #use == instead of =
      print("Person is from London")

# Calculate the factorial of a number


def factorial(n):
    if n == 0:
        return 1
    else: #add a colon
        return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))

# Create a list of numbers
numbers = range(10)
print("Numbers:", numbers)

# Print each number in the list
for num in numbers: #missing colon
    print(num)


# Define a class for a car
class Car: #missing colon
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self): #add self as a parameter
        print("Car:", self.make, self.model) #add self to access the class attributes


my_car = Car("Toyota", "Corolla")
my_car.info()

# Access class attributes directly
print("Car make:", my_car.make)
print("Car model:", my_car.model)

# Create a tuple
my_list = [1, 2, 3, 4, 5] #use square brackets instead of paranthesis
my_list[0] = 10
# Using a list instead of a tuple if you want to modify elements


# Open a file for writing
file = open('my_file.txt', 'w')
file.write("Hello, world!") #missing paranthesis

# Close the file
file.close() #missing paranthesis

# Find the length of a string
message = "Hello, world!"
length = len(message)  #len is a built-in function, not a method str

# Convert a string to uppercase
uppercase_message = message.upper() #add paranthesis for the method call
print("Uppercase message:", uppercase_message)

# Split a sentence into words
sentence = "This is a sentence"
words = sentence.split(' ') #corrected the delimiter to a space
print("Words:", words)

# Define a function to calculate the power of a number


def power(base, exponent):
    result = base ** exponent
    return result


# Calculate the power of 2 to the 3
print("2^3:", power(2, 3))

# Use a list as a stack
stack = []
stack.append(1) #use append instead of push
stack.append(2)
stack.append(3)
print("Stack:", stack)

# Pop elements from the stack
print(stack.pop())
print(stack.pop())

# Attempt to pop from an empty stack
print(stack.pop())


# Use a dictionary as a switch-case
def switch_case(case):
    return {
        'a': "Case a",
        'b': "Case b",
        'c': "Case c",
    }.get(case, "Invalid case") #added a default case


print(switch_case('b'))
print(switch_case('d'))

# Open and read a file
file = open('data.txt', 'r')
content = file.read()
print("File content:", content)

# Close the file
file.close()

# Attempt to read from a closed file
print(file.read())

# Perform division
numerator = 10
denominator = 0
result = numerator / denominator #instead denominaotr use denominator

# Print the result
print("Result:", result)

# Use a while loop to count from 1 to 5
count = 1
while count <= 5: #use colon
    print(count)
    count += 1

# Print the sum of the numbers from 1 to 10
sum = 0
for i in range(1, 11):
    sum += i #corrected the range to start from 1

print("Sum:", sum)

# Access elements of a list using an invalid index
my_list = [1, 2, 3, 4, 5]
print(my_list[10])


# Define a function that takes a default argument
def greet(name, greeting="Hello"):
    print(greeting, name)


greet("Alice")

# Swap two variables
a = 5
b = 10
a, b = b, a

# Use an invalid escape sequence in a string
invalid_string = "This is an \q invalid escape sequence"

# Print the invalid string
print(invalid_string)

# Use an invalid operator
x = 10
y = 3
result = x // y

# Print the result
print("Result:", result)

#solution and Explaination:
#count == 0 should be changed to count = 0 to properly initialize the count variable.

# avg = total / coun has a typo in the variable name. It should be count instead of coun.

# print("Average:", resul) has a typo in the variable name. It should be result instead of resul.

# if result % 2 = 0: should use == for comparison instead of =. It should be if result % 2 == 0:.

# The for loop comprehension is missing a closing square bracket. It should be squares = [num ** 2 for num in nums].

# print("Maximum square:", max_squar) has a typo in the variable name. It should be max_square instead of max_squar.

# The if statement is missing a colon at the end.

# if target_square in squares is missing a colon at the end.

# del person[city] should be del person['city'].

# for key, value in person.items: is missing parentheses after items.
# if person['city'] = 'London': should use == for comparison instead of =. It should be if person['city'] == 'London':.
# else statement is missing a colon at the end.

# print("Numbers:", number) should be print("Numbers:", numbers).

# def info() should have a colon at the end. Additionally, inside the info method, make and model should be accessed using self.make and self.model.

# my_tuple[0] = 10 tuples are immutable; you can't modify their elements after creation.

# The file write statement is missing a closing double quote.

#file.close should be file.close().

#length = str.len(message) should be length = len(message).

#message.upper should be message.upper().

# sentence.split(',') should split by spaces, not commas, to split the sentence into words.

# def power(base, exponent) is missing a colon at the end.

# result = numerator / denominaotr has a typo. It should be denominator.

# The while loop is missing a colon at the end.

# The for loop should have range(1, 11) to include numbers from 1 to 10. And, sum += 1 should be corrected to sum += i.

# print(my_list[10]) will result in an IndexError since the valid indices for my_list are 0 to 4.

# The greet function call is missing the greeting argument. It should be greet("Alice", "Hello").

# The swapping of a and b is correct but can be written more explicitly using a temporary variable.

#The string on this line contains an invalid escape sequence \q. This should be removed.

#The division operator is correct, but the comment says "Perform division," which is unnecessary.

# The while loop should have a colon at the end.
