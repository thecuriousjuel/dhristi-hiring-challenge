def generate_sequence(word_list):
    word1 = word_list[0]
    word2 = word_list[1]
    word3 = word_list[2]

    seq1 = []
    for i in range(len(word1)):
        t = word1[:i]
        if len(t) > 0:
            seq1.append(t)

    word2 = word2[1:-1]
    seq2 = []

    for i in range(len(word2)):
        for j in range(i, len(word2)):
            t = word2[i:(j + 1)]
            if len(t) > 0:
                seq2.append(t)

    seq3 = []
    for i in range(len(word3)):
        t = word3[i + 1:]
        if len(t) > 0:
            seq3.append(t)

    # print(seq1)
    # print(seq2)
    # print(seq3)

    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                print(i1 + i2 + i3)


word_list = ['apple', 'oranges', 'grapes', 'guava', 'pineapple']

generate_sequence(word_list)
