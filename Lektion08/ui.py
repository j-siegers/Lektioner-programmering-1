import os


def line(arg=False):
    if arg:
        print('*' * 30)
    else:
        print('-' * 30)


def header(text):
    text_cent = text.center(28)
    print('|' + text_cent + '|')


def echo(text):
    print('| ' + text)


def prompt(text):
    print(f'| {text} > ', end=' ')
    return input()


def clear():
    return os.system('cls')



