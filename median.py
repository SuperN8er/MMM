"""Module for working with median"""
from rand_data import get_rand_nums


def calc_median(nums):
    """Calculate the mean, given a list of numbers"""

    sorted_nums = sorted(nums)
    print(sorted_nums)
    length = len(sorted_nums)
    midpoint = length // 2

    if (length % 2) == 1:
        # odd
        median = sorted_nums[midpoint]
    else:
        # even
        lower_median = sorted_nums[midpoint-1]
        upper_median = sorted_nums[midpoint]
        median = (lower_median + upper_median) / 2

    return median


def main():
    # nums = get_rand_nums(9)
    nums = get_rand_nums(10)
    print(nums)
    print(calc_median(nums))


if __name__ == "__main__":
    main()
