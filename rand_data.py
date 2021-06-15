"""Module for creating random number lists"""
import random


def get_rand_num(mini=30, maxi=60):
    """Return a random number between mini and maxi

    default mini 30 , maxi 60

    """
    return random.randint(mini, maxi)


def get_rand_nums(loops):
    """Return a random list of numbers"""
    nums = []
    for loop in range(loops):
        nums.append(get_rand_num())

    return nums


def main():
    x = get_rand_nums(50)
    print(x)


if __name__ == "__main__":
    main()
