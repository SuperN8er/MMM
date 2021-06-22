"""Module for working with median"""
from rand_data import get_rand_nums


"""
2,3,4,5,6
3,5,2,6,4
1,2,3,4,5,6


given a list of numbers
calc the median of the list

sorting the list from low to high

find the length of list
figure if length is even or odd

if odd:
    divide the length by 2
    round the midpoint down
    median is sorted list at mid index

if even:
    upper index is divide the length by 2
    lower index is upper index minus 1
    lower median is sorted list at lower index
    upper median is sorted list at upper index
    median is lower median plus upper median divide by 2   
    
return median

"""


def calc_median(nums):
    """Calculate the mean, given a list of numbers"""

    sorted_nums = sorted(nums)
    print(sorted_nums)
    length = len(sorted_nums)

    if (length % 2) == 1:
        # odd
        midpoint = length // 2
        median = sorted_nums[midpoint]
    else:
        # even
        upper_index = length // 2
        lower_index = upper_index - 1
        lower_median = sorted_nums[lower_index]
        upper_median = sorted_nums[upper_index]
        median = (lower_median + upper_median) / 2

    return median


def main():
    # nums = get_rand_nums(9)
    nums = get_rand_nums(10)
    print(nums)
    print(calc_median(nums))


if __name__ == "__main__":
    main()
