import prompt

ROUND = 3


def run(game):
    wrong_answer = """'{0}' is wrong answer ;(. Correct answer was '{1}'.\n
    Let's try again, {2}!"""
    print("Welcome to the Brain Games!")
    print()
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
    print()
    print(game.DESCRIBER)
    for _try_num in range(0, ROUND):
        expression, result = game.run_game()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(wrong_answer.format(answer, result, name))
            break
        print('Correct!')
    else:
        print('Congratulations, ', name, '!')
