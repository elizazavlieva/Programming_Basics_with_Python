annies_book = input()
count = 0
while True:
    book_name = input()
    if book_name == 'No More Books':
        print('The book you search is not here!\n'
              'You checked {count} books.')
        break
    if book_name == annies_book:
        print(f'You checked {count} books and found it.')
        break
    count += 1

