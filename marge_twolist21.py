def mergeTwoLists(list1, list2):
    marge=list1+list2
    marge.sort()
    return marge

list1=[1,2,4]
list2=[1,3,4]

print(mergeTwoLists(list1, list2))




# def mergeTwoLists(list1, list2):
#     # Create a new list that combines both lists
#     merged_list = list1 + list2
#     # Sort the merged list
#     merged_list.sort()
#     return merged_list

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# print(mergeTwoLists(list1, list2))
