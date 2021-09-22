def main():
    import time
    import random
    import mostx
    langs = tuple(mostx.get_available_langs())
    while (lang := input(f"choose language from ({', '.join(langs)}):")) not in langs:
        print("error: unsupported language")
    qgen = mostx.QuizGenerator(lang=lang)
    time.sleep(.2)
    print("OK! Game Start!")
    time.sleep(.2)
    while True:
        print("\n")
        quiz = qgen.gen_mostx_quiz(choices='ABC', n_adjs=random.choice([1, 2, 3]))
        print('\n'.join(quiz.statements))
        while not(user_pred := input(f"{quiz.question}:")):
            print("error: invalid input")
        user_pred = user_pred.upper()
        if user_pred == quiz.answer:
            print('CORRECT')
        else:
            print('INCORRECT')



if __name__ == '__main__':
    main()