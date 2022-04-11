import random


class Apple:
    amount = 0
    weight = 0

    def __init__(self, weight):
        Apple.amount += 1
        Apple.weight += weight


def main():
    while (Apple.amount <= 1000 and Apple.weight <= 300):
        Apple(random.uniform(0.2, 0.5))
    print("Process stop with {} and wieghts {:.2f}".format(Apple.amount, Apple.weight))

main()