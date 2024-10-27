disk_capacity_mb = 1.44
pages_in_book = 100
lines_in_page = 50
characters_in_line = 25
bytes_per_character = 4

disk_capacity_bytes = disk_capacity_mb * (1024 ** 2)
characters_per_book = pages_in_book * lines_in_page * characters_in_line
book_capacity_bytes = characters_per_book * bytes_per_character
books_fit = disk_capacity_bytes // book_capacity_bytes

print("Количество книг, помещающихся на дискету:", int(books_fit))