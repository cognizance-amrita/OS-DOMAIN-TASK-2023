def fibonacci_sequence(n):
    fibonacci = []
    a, b = 0, 1
    for i in range(n):
        fibonacci.append(a)
        a = b
        b = a + b
    return fibonacci

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i = 0:
            return False
    return True

def analyze_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    prime_count = 0
    for num in numbers:
        if num % 2 = 0:
            even_sum += num
        else:
            odd_sum += num
        if is_prime(num):
            prime_count += 1
    return even_sum, odd_sum, prime_count

numbers = [2, 5, 8, 13, 18, 21, 25, 29, 32, 37]
even_sum, odd_sum, prime_count = analyze_numbers(numbers)
fibonacci_sequence = fibonacci_sequence(10)
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)
print("Number of Primes:", prime_count)
print("Fibonacci Sequence:", fibonacci_sequence)
