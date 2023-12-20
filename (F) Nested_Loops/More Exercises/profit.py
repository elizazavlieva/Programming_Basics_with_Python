one_leva_count = int(input())
two_leva_count = int(input())
five_leva_count = int(input())
total_leva = int(input())


for one_leva in range(one_leva_count + 1):
    for two_leva in range(two_leva_count + 1):
        for five_leva in range(five_leva_count + 1):
            if one_leva + (two_leva * 2) + (five_leva * 5) == total_leva:
                print(f"{one_leva} * 1 lv. + {two_leva} * 2 lv. + {five_leva} * 5 lv. = {total_leva} lv.")
