score = 0
question = 5

print('Quiz time!!!')
print(' ')

# Q1
print('Q1. What is the largest organ in the human body?')
Q1 = input('Your Answer: ')

if Q1 == 'skin':
    print('Currect!!!')
    score = 1
else:
    print('Incorrect, the answer is skin.')
print(' ')

# Q2
print('Q2. What is 7(34-60)/13')
Q2 = int(input('Your Answer: '))

if Q2 == -14:
    print('Currect!!!')
    score = score + 1
else:
    print('Incorrect, the answer is -14.')
print(' ')

# Q3
print('Q3. What is the capital of France? (Capitalize the frist letter)')
Q3 = input('Your Answer: ')

if Q3 == 'Paris':
    print('Currect!!!')
    score = score + 1
else:
    print('Incorrect, the answer is Paris.')
print(' ')

# Q4
print('Q4. Where is the most populous country in the would? ')
print('A. China')
print('B. India')
print('C. USA')
print('D. Brasil')
Q4 = input('Your Answer: ')

if Q4 == 'B':
    print('Currect!!!')
    score = score + 1
else:
    print('incorrect, the answer is India.')
print(' ')

# Q5
print('Q5. What is the longest river in the would? ')
print('A. Amazon')
print('B. Yanftze')
print('C. Mississippi')
print('D. The Nile')
Q5 = input('Your Answer: ')

if Q5 == 'D':
    print('Currect!!!\n')
    score = score + 1
else:
    print('incorrect, the answer is India.\n')



percent = score / question * 100
print(f'Congratulations, you got {score} answers right.')
print(f'That is a score of {percent}%.')