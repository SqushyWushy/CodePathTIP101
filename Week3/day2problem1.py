"""
purpose of program: we want to take a list of string integers and calculate the total sum
step 1: declare a list for integers and declare an integer variable with the final sum
step 2: run through the list of string integers and convert each into a regular integer
step 3: add each new converted integer into the earlier declared list for our integers
step 4: return the sum of the new integer list

"""


def sum_of_number_strings(num_strings):
    list_nums = []
    for num in num_strings:
        list_nums.append(int(num))
    return sum(list_nums)


nums = ["21", "32", "45", "78"]
result = sum_of_number_strings(nums)
print(result)
