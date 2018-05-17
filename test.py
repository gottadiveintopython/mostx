# -*- coding: utf-8 -*-
import mostx

langs = tuple(mostx.langs())
print(langs)


def print_quiz(quiz):
    print(
        r'------------------------------------',
        *quiz.statements,
        'choices: ' + str(quiz.choices),
        'answer: ' + str(quiz.answer),
        sep='\n')


for lang in langs:
    quiz = mostx.generate_quiz(
        choices='ABC',
        n_adjectives=1,
        lang=lang)
    print_quiz(quiz)

    quiz = mostx.generate_quiz(
        choices=('Python', 'JavaScript', 'Swift', 'Java', ),
        n_adjectives=2,
        lang=lang)
    print_quiz(quiz)

    quiz = mostx.generate_quiz(
        choices=range(3),
        n_adjectives=1,
        lang=lang)
    print_quiz(quiz)

