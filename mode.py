"""Module for working with mode"""
from rand_data import get_rand_nums


def calc_mode(nums):
    """Calculate the mean, given a list of numbers"""

    nums_counts = []
    for uniq_num in set(nums):
        num_count = nums.count(uniq_num)
        nums_counts.append((num_count, uniq_num))

    nums_counts.sort(reverse=True)
    return nums_counts[0][1]


def main():
    nums = get_rand_nums(10, mini=1, maxi=10)
    print(nums)
    print(calc_mode(nums))


if __name__ == "__main__":
    main()
