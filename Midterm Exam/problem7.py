def score(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_word = word.lower()
    highest_score = 0
    second_highest_score = 0
    for i in range(len(lower_word)):
        score = (alphabet.index(lower_word[i])+1) * i
        print('score: ' + str(score))
        if score > highest_score:
            second_highest_score = highest_score
            highest_score = score
        elif score > second_highest_score:
            second_highest_score = score
    print('Highest score: %d, Second highest: %d' % (highest_score, second_highest_score))


score('adDZgh')