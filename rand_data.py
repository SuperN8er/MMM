"""Module for creating random number lists"""
import random


def get_rand_nums(loops, mini=30, maxi=60):
    """Return a random list of numbers"""
    nums = []
    for loop in range(loops):
        rand_num = random.randint(mini, maxi)
        nums.append(rand_num)

    return nums


def main():
    x = get_rand_nums(25)
    print(x)


if __name__ == "__main__":
    main()
