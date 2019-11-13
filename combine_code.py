def combine(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    combo = []
    if len1 > len2:
        i = 0
        while i < len2:
            combo.append(list1[i])
            combo.append(list2[i])
            i = i + 1
        for remaining_index in range(i,len1):
            combo.append(list1[remaining_index])
    elif len1 < len2:
        i = 0
        while i < len1:
            combo.append(list1[i])
            combo.append(list2[i])
            i = i + 1
        for remaining_index in range(i,len2):
            combo.append(list2[remaining_index])
    else:
        if len1 == len2:
            for i in range(len1):
                combo.append(list1[i])
                combo.append(list2[i])
    return combo

combined = combine([11,22,33], [1,2,3])
print(combined)
