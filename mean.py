"""Module for working with mean"""
from rand_data import get_rand_nums


"""
given a list of numbers
calc the mean of the list

add all numbers on list and store in var
find len of list and store in var

mean equals divide the sum by len
return mean

"""


def example(nums):
    total = 0
    for num in nums:
        total += num

    return total


def example_two(nums):
    length = 0
    for _ in nums:
        length += 1

    return length


def calc_mean(nums):
    """Calculate the mean, given a list of numbers"""
    total = sum(nums)
    length = len(nums)
    mean = total / length
    return mean


def main():
    nums = get_rand_nums(3)
    print(nums)
    print(sum(nums))
    print(len(nums))
    print(calc_mean(nums))


if __name__ == "__main__":
    main()
