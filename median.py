"""Module for working with median"""


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


def main():
    pass


if __name__ == "__main__":
    main()
