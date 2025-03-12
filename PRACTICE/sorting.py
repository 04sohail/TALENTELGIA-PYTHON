# lst = [23, 65, 78, 26, 56, 67, 12]

# SELECTION SORT ASCENDING ORDER
# def selection_sort_asc(lst):
#     for i in range(0, len(lst)):
#         minIndex = i
#         for j in range(i, len(lst)):
#             if lst[j]<lst[minIndex]:
#                 minIndex = j
#         lst[i],lst[minIndex] = lst[minIndex], lst[i]
#     print(lst)
# SELECTION SORT DESCENDING ORDER
# def selection_sort_desc(lst):
#     for i in range(0, len(lst)):
#         maxIndex = i
#         for j in range(i, len(lst)):
#             if lst[j] > lst[maxIndex]:
#                 maxIndex = j
#         lst[i], lst[maxIndex] = lst[maxIndex], lst[i]
#     print(lst)

# print("-"*50)
# print("SELECTION SORT ASCENDING")
# selection_sort_asc(lst)
# print("-"*50)
# print("SELECTION SORT DESCENDING")
# selection_sort_desc(lst)
# print("-"*50)







lst = [23, 65, 78, 26, 56, 67, 12]

# BUBBLE SORTING ASCENDING
def bubble_sort_asc(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)

bubble_sort_asc(lst)
