"""
#1,write  a python function to sort the given input list containing strings of format
#  "Student_id-age-marks". Sorgting should be based on  marks obtainedby each student
#  if student have same marks then sort based on student_id.

    
    sample Output:["S104-23-20","S102-24-23","S105-23-23","S101-23-45","S103-23-62"]

"""
"""
input_x = ["S101-23-45","S102-24-23","S103-23-62","S104-23-20","S105-23-23"]

y = list(sorted(input_x, key=lambda x: x.split("-")[-1]))

print(y)
"""

### OUR OWN LOGIC
"""

input_x = ["S101-23-45","S102-24-23","S103-23-62","S104-23-20","S105-23-23"]


for i in range(0, len(input_x)):
    input_x[i] = tuple(input_x[i].split("-"))

print(input_x)



for data in input_x:
    ele = data[-1]


"""  
