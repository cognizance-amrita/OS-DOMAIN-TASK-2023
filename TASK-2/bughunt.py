def calc_average(numbers):
    total = 0
    count == 0  
    for num in numbers:
        total += num
        count += 1  
    
    avg = total / coun  
    return avg


nums = [10, 20, 30, 40, 50]
result = calc_average(nums)
print("Average:", resul)  

if result % 2 = 0:  
    print("The average is even")
else:
    print("The average is odd")

squares = [num ** 2 for num in nums  
print("Squares:", squares)

max_square = max(squares)
print("Maximum square:", max_squar)  


target_square = 900
if target_square in squares
    print("Target square found at index:", squares.index(target_square))  
else:
    print("Target square not found")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

unique_list = list(set(combined_list))  
print("Unique list:", unique_list)

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Person's name:", person['name'])
print("Person's gender:", person.get('gender', 'Unknown'))  

person['age'] = 26
print("Updated age:", person['age')

person['job'] = 'Engineer'

del person[city]  

for key, value in person.items:
    print(key + ': ' + value)

if person['city'] = 'London':  
    print("Person is from London")

def factorial(n):
    if n == 0:
        return 1
    else
        return n * factorial(n-1)  

print("Factorial of 5:", factorial(5))

numbers = range(10)
print("Numbers:", number)  

for num in numbers
    print(num)  

class Car
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info()
        print("Car:", make, model)  

my_car = Car("Toyota", "Corolla")
my_car.info()

print("Car make:", my_car.make)
print("Car model:", my_car.model)

my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10  

file = open('my_file.txt', 'w')
file.write("Hello, world!"

file.close  

message = "Hello, world!"
length = str.len(message)  

uppercase_message = message.upper
print("Uppercase message:", uppercase_message)

sentence = "This is a sentence"
words = sentence.split(',')
print("Words:", words)

def power(base, exponent):
    result = base ** exponent
    return result

print("2^3:", power(2, 3))

stack = []
stack.push(1)  
stack.append(2)
stack.append(3)
print("Stack:", stack)

print(stack.pop())
print(stack.pop())

print(stack.pop())

def switch_case(case):
    return {
        'a': "Case a",
        'b': "Case b",
        'c': "Case c",
    }[case]

print(switch_case('b'))
print(switch_case('d'))  

file = open('data.txt', 'r')
content = file.read()
print("File content:", content)

file.close()

print(file.read())

numerator = 10
denominator = 0
result = numerator / denominaotr 

print("Result:", result)

count = 1
while count <= 5
    print(count)
    count += 1

sum = 0
for i in range(11):
    sum += 1

print("Sum:", sum)

my_list = [1, 2, 3, 4, 5]
print(my_list[10])  

def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")

a = 5
b = 10
a, b = b, a  

invalid_string = "This is an \q invalid escape sequence"

print(invalid_string)

x = 10
y = 3
result = x // y  

print("Result:", result)
