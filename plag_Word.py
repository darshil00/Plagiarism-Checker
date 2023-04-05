def similar_Sentence(check_Sentence_1, check_Sentence_2,percent):
    plag_words = 0
    check_word_1 = check_Sentence_1.split(' ')
    #print(check_word_1)
    check_word_2 = check_Sentence_2.split(' ')
    count_x = 0  # PUNE GANDU YE REITERATION KE LIYE HAI
    count_y = 0
    iterate_checkWord2 = []
    iterate_checkWord2.append(check_word_2[0])
    for x in check_word_1:
        count_x+=1
        for y in iterate_checkWord2:
            if x == y:
                if len(check_word_1) > len(check_word_2):
                    plag_words = plag_words + 1 / len(check_word_1)
                elif len(check_word_2) > len(check_word_1):
                   plag_words = plag_words + 1 / len(check_word_2)
        if count_x == len(check_word_1):
            iterate_checkWord2.append(check_word_2[count_y])
            count_y += 1
    if plag_words > percent:#x=sentence ka % allowed
        return True
    else:
        return False