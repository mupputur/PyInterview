# Question2
"""
Write a python program to transpose a given table or matrix
Example:

Input:
    [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
Output:
    [, 41, 23, 251, 231, 321, 91, 0]
"""

##################################################################
#Using zip() function
##################################################################

input_x = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
print("Input : {}".format(input_x))
output_y = list(zip(*input_x))
print("Output: {}".format(input_x))



##################################################################
# Wrire your own logic
"""
Assume its like a matrix of size 3 X 4
We have  to make it 4 X 3 by changing its rows to columns and columns to row
"""
##################################################################

input_x = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
output_y = []
for i in range(len(input_x[0])):
    y = []
    for sub_list in input_x:
        y.append(sub_list[i])
    #print(y) debug
    output_y.append(y)
print("Output: {}".format(input_x))

##################################################################
#Using numpy module
##################################################################
import numpy

input_x = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
output_y = numpy.transpose(input_x)
print


    
