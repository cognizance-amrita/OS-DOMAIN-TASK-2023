Welcome to the Bug Finding and Fixing Challenge!:space_invader: In this task, you'll be presented with code snippets containing bugs and errors. Your objective is to identify the problems and provide appropriate solutions.:detective: This exercise will help you sharpen your debugging skills and gain valuable experience in analyzing and rectifying code issues.:sunglasses: 
## Instructions: :memo:
1. Identify the issues in the provided challenge code. 
2. Explain the problem and provide a detailed solution. 
4. Some bugs may be complex; feel free to ask for hints if needed. 
5. Submit your solutions for evaluation.
## Example code snippet: :bulb:
    def calculate_average(numbers): 
    total = 0 
    count = 0 
    for num in numbers: 
        total += num 
    average = total / count 
    return average 
    numbers = [25, 30, 35, 40, 45] 
    result = calculate_average(numbers)
    print("Average:", result) 
## Issues: :warning:
- count is not being incremented, resulting in division by zero.
- The average calculation formula is incorrect.
## Solution: :mag_right:
    def calculate_average(numbers): 
    total = 0 
    count = len(numbers)  # Increment the count 
    for num in numbers: 
        total += num 
    average = total / count 
    return average 
    numbers = [25, 30, 35, 40, 45] 
    result = calculate_average(numbers) 
    print("Average:", result) 
## Evaluation Criteria: :bar_chart:
1. Accuracy and correctness of bug identification and fixes.
2. Clarity and completeness of problem descriptions and solutions.
3. Proper application of Python syntax and conventions.
4. Quality of explanations in the bug fixes.

## Challenge Code
[Bug Hunt](https://github.com/cognizance-amrita/OS-DOMAIN-TASK-2023/blob/main/bughunt.cpp)


Feel free to reach out if you have any questions. Good luck, and happy bug hunting!




  


