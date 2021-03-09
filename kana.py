import argparse
import numpy as np

from key import COLUMNS


def clean(arg_value):
    """
    clean_str_args: Str -> Str
    requirements: arg_value must be a string
    cleans passed string argument values so things work later on
    """
    return arg_value.strip().lower()


def evaluate(guess, score, kana, answer_key):
    """
    evaluate a guess from the user
    """
    if guess == answer_key[kana]['sound']:
        print('Correct!')
        return score+1
    response = clean(input('Nope. Try again ([y]/n)? '))

    if response not in ['y', 'n', '']:
        response = input('Please enter either y or n: ')

    if response == 'n':
        as_in = f'(as in {answer_key[kana]["as_in"]})'
        print(f'Answer -> {kana}: {answer_key[kana]["sound"]} {as_in}')
        return score
    guess = clean(input(f'{kana}: '))
    return evaluate(guess, score, kana, answer_key)


def main():
    parser = argparse.ArgumentParser(
        description='Practice Japanese Kanas in different scripts')
    parser.add_argument('-c', '--column', default='a', type=str,
        help='Columns to practice e.g. a/k/s (default: a)')
    parser.add_argument('-s', '--script', default='hiragana', type=str,
        help='Scripts to include e.g. hiragana/katana/kanji (default: hiragana)')
    args = parser.parse_args()

    # answer dictionary
    key = COLUMNS[clean(args.column)][clean(args.script)]
    to_practice = list(key.keys())
    np.random.shuffle(to_practice)

    score = 0
    for kana in to_practice:
        ans = clean(input(f'{kana}: '))
        score = evaluate(ans, score, kana, key)

    print(f'Your score: {score}/{len(to_practice)}')



if __name__ == '__main__':
    main()
