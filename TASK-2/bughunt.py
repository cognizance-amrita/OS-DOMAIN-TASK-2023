def calc_average(numbers):
    total = 0
    count == 0  
    for num in numbers:
        total += num
        count += 1  
    avg = total / coun 
    return avg

# Test the function
nums = [10, 20, 30, 40, 50]
result = calc_average(nums)
print("Average:", resul) 
# Check if the average is even or odd
if result % 2 = 0:  
    print("The average is even")
else:
    print("The average is odd")

# Generate a list of squares
squares = [num ** 2 for num in nums  
print("Squares:", squares)

# Find the maximum square
max_square = max(squares)
print("Maximum square:", max_squar)  

# Search for a specific square
target_square = 900
if target_square in squares
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
print("Updated age:", person['age')

# Add a new key-value pair
person['job'] = 'Engineer'

# Delete the city key
del person[city] 

# Print all key-value pairs in the dictionary
for key, value in person.items:
    print(key + ': ' + value)

# Check if person is from London
if person['city'] = 'London':  
    print("Person is from London")

# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else
        return n * factorial(n-1)  

print("Factorial of 5:", factorial(5))

# Create a list of numbers
numbers = range(10)
print("Numbers:", number) 

# Print each number in the list
for num in numbers
    print(num)  

# Define a class for a car
class Car
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info()
        print("Car:", make, model)  

my_car = Car("Toyota", "Corolla")
my_car.info()

# Access class attributes directly
print("Car make:", my_car.make)
print("Car model:", my_car.model)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10  

# Open a file for writing
file = open('my_file.txt', 'w')
file.write("Hello, world!"

# Close the file
file.close 

# Find the length of a string
message = "Hello, world!"
length = str.len(message) 

# Convert a string to uppercase
uppercase_message = message.upper
print("Uppercase message:", uppercase_message)

# Split a sentence into words
sentence = "This is a sentence"
words = sentence.split(',')
print("Words:", words)

# Define a function to calculate the power of a number
def power(base, exponent):
    result = base ** exponent
    return result

# Calculate the power of 2 to the 3
print("2^3:", power(2, 3))

# Use a list as a stack
stack = []
stack.push(1)  
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
    }[case]

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
result = numerator / denominaotr  

# Print the result
print("Result:", result)

# Use a while loop to count from 1 to 5
count = 1
while count <= 5
    print(count)
    count += 1

# Print the sum of the numbers from 1 to 10
sum = 0
for i in range(11):
    sum += 1

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
