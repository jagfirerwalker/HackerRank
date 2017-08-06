def return_union(list_a, list_b):
    len1 = len(list_a)
    len2 = len(list_b)
    final_sorted_list = []
    j = 0
    k = 0

    for i in range(len1+len2):
        if k == len1:
            final_sorted_list.extend(list_b[j:])
            break
        elif j == len2:
            final_sorted_list.extend(list_a[k:])
            break
        elif list_a[k] < list_b[j]: #iterate over the the list and check if list b item is bigger than list a item
            final_sorted_list.append(list_a[k])
            k += 1

        else:
            final_sorted_list.append(list_b[j])
            j += 1
            
    return final_sorted_list

list1 = input('List1: ')
list2 = input('List2: ')
print(return_union(list1, list2))
