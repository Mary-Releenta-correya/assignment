def largest(list):
    large=list[0]
    for i in list:
        if i>large:
            large=i
    return large
list=[45,56,98,3,67,9,90]
print("largest number is",largest(list))