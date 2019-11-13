def frame(words):
    #find the longest word first
    len_words = len(words)
    longest = words[0]
    for i in range(len_words):
        if len(words[i]) >= len(longest):
            longest = words[i]

    len_longest = len(longest)
    len_row = len_longest + 4
    print("*"*len_row)

    for i in range (len_words):
        word_row = "* " + words[i]
        if len(word_row) < len_row + 2:
            while len(word_row) < len_row-1:
                word_row = word_row + " "
            word_row = word_row + "*"
            print(word_row)
            continue
        word_row = word_row + " *"
        print(word_row)
    print("*"*len_row)

frame(["Write","good","code","every","day"])
