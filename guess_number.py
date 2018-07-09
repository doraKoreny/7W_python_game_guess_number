import random


def guess_number(lowest, highest):
    return random.randint(lowest, highest)


def main():
    guess_number(1, 20)


if __name__ == '__main__':
    main()
