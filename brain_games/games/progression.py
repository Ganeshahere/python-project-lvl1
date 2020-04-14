from random import randint

describer = 'What number is missing in the progression?'


def run_game():
    number1 = randint(1, 99)
    step = randint(1, 99)
    hidden_number = randint(0, 9)
    counter = 0
    progression = ''

    while counter < 10:
        curnumber = number1 + (counter * step)

        if counter == hidden_number:
            element = '.. '
            result = str(curnumber)
        else:
            element = str(curnumber) + " "

        progression += element
        counter += 1

    expression = '{}'.format(progression)

    return expression, result
