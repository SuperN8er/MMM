"""Module for working with mean"""
from rand_data import get_rand_nums


def calc_mean(nums):
    """Calculate the mean, given a list of numbers"""

    return sum(nums) / len(nums)


def main():
    nums = get_rand_nums(3)
    print(nums)
    print(sum(nums))
    print(len(nums))
    print(calc_mean(nums))


if __name__ == "__main__":
    main()
