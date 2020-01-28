from Multiquestions import Question

#created new python file "MULTIQUESTIONS.PY"
'''********THIS VERSION IS BROKEN'''

question_prompts = [
    "What colour are apples?\na. red\nb. blue \nc. orange\n\n",
    "What colour are bananas?\na. red\nb. yellow \n c. orange\n\n",
    "What colour are blueberries?\na. red\nb. blue \n c. orange\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + '/' + str(len(questions) + "correct"))

run_test(questions)

