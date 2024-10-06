def reverse_string(my_str):
    reverse_lst = []
    list_str = list(my_str)

    for i in range(len(list_str) - 1, -1, -1):
        reverse_lst.append(list_str[i])

    reverse_str = "".join(reverse_lst)
    return reverse_str


print(reverse_string("Hello"))
