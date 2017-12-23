import random
import os
from _datetime import datetime


def clearscreen(numlines=100):
    """Clear the console. numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def extract_wisdom():
    """Reads wisdoms from the wisdom.txt file and returns tree random ones"""
    with open("wisdoms.txt", 'r', encoding='utf-8') as wisdoms:
        return random.sample(wisdoms.readlines(), 5)


def print_resolutions():
    """print resolutions for the year. Must be a single line"""
    print('#')
    with open("resolutions.txt", 'r', encoding='utf-8') as values:
        print('#   Resolutions for {}: '.format(datetime.today().year), values.readline())


def print_values():
    """print values for the year. Must be a single line"""
    print('#')
    with open("values.txt", 'r', encoding='utf-8') as values:
        print('#   VALUES: ', values.readline())


def print_wisdoms():
    """beauty prints random wisdoms"""
    number_of_sharps = 120
    print('#' * number_of_sharps)
    print_values()
    print_resolutions()
    print('#')
    for winsdom in extract_wisdom():
        print('#  ', winsdom.rstrip())
        print('#')
    print('#' * number_of_sharps)
    print()


def get_answers():
    """Read all lines from questions.txt, asks them and saves the answers
    returns a list of tuples (question, answer)
    """
    answered_q = []
    with open("questions.txt", 'r', encoding='utf-8') as questions:
        for question in [x.rstrip() for x in questions.readlines()]:
            print()
            print(question)
            answer = input("A:  ")
            answered_q.append((question, answer))
    return answered_q


def store_answered(answered_q):
    """Writes a list of tuples (question, answer) to a folder ./store/*YEAR*/*MONTH*/*DAY*.txt"""
    today = datetime.today()
    folder = "store" + "/" + str(today.year) + "/" + str(today.month)
    os.makedirs(folder, exist_ok=True)
    filename = folder + "/" + str(today.day) + ".txt"
    with open(filename, "a", encoding="utf-8") as outfile:
        for question, answer in answered_q:
            outfile.write(question + '\n')
            outfile.write(answer + '\n\n')


if __name__ == "__main__":
    clearscreen()
    print_wisdoms()
    answered = get_answers()
    clearscreen()
    for q, a in answered:
        print(q)
        print(a)
    store_answered(answered)
