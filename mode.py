"""Module for working with mode"""
from rand_data import get_rand_nums


"""
given a list of numbers
calculate the mode of the list

get unique list of numbers from given list

********* GOAL FOR THE LOOP *************
**collect pairs of unique numbers and their count**

loop through unique numbers
    find count of unique number in given list
    pair the count with the unique number
    append pair to collection

sort the collection in reverse order
get the first element in the collection
then get the second element from the pair AKA the mode
return mode

"""


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
