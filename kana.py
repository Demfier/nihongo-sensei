import argparse
import numpy as np
from collections import Counter

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


def get_kanas(columns_val, scripts_val):
    """
    returns all the correct kanas the user wishes to practice based on input
    arguments columns and scripts
    """
    # answer dictionary
    key = {}
    columns_val = clean(columns_val)
    if columns_val == 'all':
        column_chars = COLUMNS.keys()
    else:
        column_chars = columns_val.split(',')

    if scripts_val == 'all':
        scripts = ['hiragana', 'katakana']
    else:
        scripts = clean(scripts_val).split(',')

    # fetch all desired kanas
    for c in column_chars:
        for s in scripts:
            key.update(COLUMNS[c][s])
    return key


def main():
    parser = argparse.ArgumentParser(
        description='Practice Japanese Kanas in different scripts')
    parser.add_argument('-c', '--column', default='all', type=str,
        help='Columns to practice e.g. a/k/s (default: all)')
    parser.add_argument('-s', '--script', default='hiragana', type=str,
        help='Scripts to include e.g. hiragana/katakana (default: hiragana)')
    parser.add_argument('-n', '--number', default=50, type=int,
        help='Number of kanas to practice (default: 50)')
    args = parser.parse_args()

    key = get_kanas(args.column, args.script)

    to_practice = np.random.choice(list(key.keys()), size=args.number)

    score = 0
    for kana in to_practice:
        ans = clean(input(f'{kana}: '))
        score = evaluate(ans, score, kana, key)

    print(f'Your score: {score}/{len(to_practice)}')



if __name__ == '__main__':
    main()
