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
    """Reads wisdoms from the wisdom.txt file and returns a random one"""
    with open("wisdoms.txt", 'r', encoding='utf-8') as wisdoms:
        return random.choice(wisdoms.readlines())


def print_wisdom():
    """beauty prints a random wisdom"""
    number_of_sharps = 80
    print('#' * number_of_sharps)
    print('#')
    print('#  ', extract_wisdom().rstrip())
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
    print_wisdom()
    answered = get_answers()
    clearscreen()
    for q, a in answered:
        print(q)
        print(a)
    store_answered(answered)
