import listmaker

def merge_lists(list1, list2, merged=[]):
    if len(list1) == 0:
        merged.extend(list2)
        return merged
    elif len(list2) == 0:
        merged.extend(list1)
        return merged
    if list1[0] <= list2[0]:
        merged.append(list1[0])
        return merge_lists(list1[1:], list2, merged)
    elif list2[0] < list1[0]:
        merged.append(list2[0])
        return merge_lists(list1, list2[1:], merged)

print(merge_lists(listmaker.create_sorted_list(200), listmaker.create_sorted_list(200)))