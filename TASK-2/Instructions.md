Welcome to the Bug Finding and Fixing Challenge!:space_invader: In this task, you'll be presented with a challenge code containing bugs and errors. Your objective is to identify the problems and provide appropriate solutions.:detective: This exercise will help you sharpen your debugging skills and gain valuable experience in analyzing and rectifying code issues.:sunglasses: 
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

## Challenge Code :star:
[Bug Hunt](https://github.com/cognizance-amrita/OS-DOMAIN-TASK-2023/blob/main/TASK-2/bughunt.cpp)

## Submission: :mailbox_with_mail:
1. On the top right corner of the repository's page, you'll find a "Fork" button. Click on it.
2. A popup will appear, asking where you want to fork the repository. By default, your personal GitHub account should be selected. Click on your username to fork the repository to your account.
3. GitHub will create a copy of the repository in your account.
4. Once the forking process is complete, you will be redirected to your forked repository's page. The repository name will include your GitHub username to differentiate it from the original repository.
5. Navigate to your copy of the repository, create a branch and name it "submission"
6. Navigate to the submission directory
7. In the directory create a new directory called "task-2"
8. Inside "task-2", create a file named "bughuntsol.py"
9. Fill in the file with your solution to the challenge code
10. Commit changes
11. Create a new pull request from your "submission" branch to "main" branch of the original repository
12. Don't merge the pull request yet!

   
Feel free to reach out if you have any questions. Good luck, and happy bug hunting!




  


