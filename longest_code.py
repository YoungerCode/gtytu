def longest(words):
    # stop executing the function if the words list is empty
    if(len(words) == 0):
        return

    longest_words = []
    current_longest_word = words[0]
    longest_words.append(current_longest_word)
    for i in range(1,len(words)):
        if len(words[i]) > len(current_longest_word):
            current_longest_word = words[i]
            longest_words.clear()
            longest_words.append(current_longest_word)
        elif len(words[i]) == len(current_longest_word):
            longest_words.append(words[i])
        else:
            continue

    for i in range(len(longest_words)):
        print(longest_words[i] + "\n")


# tests
print ("list one test")
list1 = ["the","quick","brown", "fox", "ate", "my", "chickens"]
print(list1)
longest(list1)
list2 = ["once", "upon", "a", "time"]
print("List two test")
print(list2)
longest(list2)
print("testing empty list")
longest([])
