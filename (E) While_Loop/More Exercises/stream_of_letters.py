count_n = 0
count_o = 0
count_c = 0
word = ''
secret_word = ''
while True:
    letter = input()
    if letter == 'End':
        print(secret_word)
        break
    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:

        if letter == 'n':
            count_n += 1
            if count_n > 1:
                word += letter
                count_n = 1
        elif letter == 'c':
            count_c += 1
            if count_c > 1:
                word += letter
                count_c = 1
        elif letter == 'o':
            count_o += 1
            if count_o > 1:
                word += letter
                count_o = 1
        else:
            word += letter
        if (count_o + count_c + count_n) == 3:
            secret_word += word
            secret_word += ' '
            word = ''
            count_o = 0
            count_c = 0
            count_n = 0