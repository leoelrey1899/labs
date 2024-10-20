# TODO Найдите количество книг, которое можно разместить на дискете
one_smb = 4
one_str = one_smb * 25
one_page = one_str * 50
one_book = one_page * 100
discet_kb = 1.44
discret_bt = discet_kb * 1024 * 1024
number_of_books = discret_bt // one_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
