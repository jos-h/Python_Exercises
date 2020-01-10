"""

    Program to find pair who sums
    equal the give input
"""


def find_pairs(arr, input_sum):
    """

    :param arr:  given array of integers
    :param input_sum:  integer sum to check
    prints the pairs whose addition equals the
    input_sum
    """
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == input_sum:
                print(f"{arr[i]} + {arr[j]} = {input_sum}")
            j += 1
        i += 1


def find_pairs_optimal_approach(arr, input_sum):
    """

    :param arr:  given array of integers
    :param input_sum:  integer sum to check
    prints the pairs whose addition equals the
    input_sum
    """
    element_dict = dict()
    for each in arr:
        difference = abs(each - input_sum)
        if difference in element_dict and each < input_sum:
            print(f"{each} + {difference} = {input_sum}")
        elif each not in element_dict:
            element_dict[each] = 1
        else:
            element_dict[each] += 1


def find_pairs_ii(arr, input_sum):
    """

        :param arr:  given array of integers
        :param input_sum:  integer sum to check
        prints the pairs whose addition equals the
        input_sum
        """
    arr.sort()
    start_pos = 0
    end_pos = len(arr) - 1
    while start_pos < end_pos:
        addition = arr[start_pos] + arr[end_pos]
        if addition == input_sum:
            print(f"{arr[start_pos]} + {arr[end_pos]} = {input_sum}")
        if addition < input_sum:
            start_pos += 1
        else:
            end_pos -= 1


def main():
    """

    Function calling and input declaration
    happens here
    """
    arr = [7, 3, 2, 1, 4, 6, 8, 9, 10, 11, 0]
    # time complexity is O(n^2)
    find_pairs(arr, 11)

    # another approach
    print("Another approach using python dictionary")
    find_pairs_optimal_approach(arr, 11)

    print("Solving it using Binary Search")
    # Another approach
    find_pairs_ii(arr, 11)


if __name__ == '__main__':
    main()
