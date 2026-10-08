import random

from quiz_questions import questions

def scattered():
    random.shuffle(questions)

def display_question(each_question, idx):
    print(f"{idx}. {each_question['question']}\n")

def display_option(each_question):
    for every_option in each_question['options']:
        print(every_option)

def get_answer():
    users_choice = input('\nYour answer: ').strip().upper()
    return users_choice

def validation(users_choice):
    allowed_options = ['A', 'B', 'C', 'D']
    while users_choice not in allowed_options:
        print('Re-choose from the options listed above')
        users_choice = get_answer()
    return users_choice


Total_score = 0 

def check_answer(each_question, users_choice):
    global Total_score
    if users_choice == each_question['answer']:
        print('Result: Correct')
        Total_score += 1
        
    else:
        print('Result: Incorrect')
scattered()
for idx, each_question in enumerate(questions, 1):
    display_question(each_question, idx)
    display_option(each_question)
    users_choice = get_answer()
    users_choice = validation(users_choice)
    check_answer(each_question, users_choice)
percentage_score = round((Total_score/len(questions))*100, 2)
print(f'Your Total score is {Total_score} out of {len(questions)}')
print(f'Your Total percentage score is for this quiz is {percentage_score}%')
