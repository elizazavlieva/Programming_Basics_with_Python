book_pages, pages_per_hour, days = int(input()), int(input()), int(input())
result = (book_pages // pages_per_hour) // days
print(result)
