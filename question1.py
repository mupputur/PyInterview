# Question1
"""
Write a python program to remove all duplicate values from the given input list

Example:

Input:
    [11, 41, 23, 41, 251, 231, 321, 251, 91, 0, 41, 251, 321]
Output:
    [11, 41, 23, 251, 231, 321, 91, 0]
"""

def remove_dups(x):
    unique_list = []
    for e in x:
        if e not in unique_list:
            unique_list.append(e)
    return unique_list


if __name__ == "__main__":
    # Test Code
    x = [11, 41, 23, 41, 251, 231, 321, 251, 91, 0, 41, 251, 32]
    print(remove_dups(x))
    
