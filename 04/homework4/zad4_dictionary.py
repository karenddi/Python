# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

numbers1 = range(1,11)
numbers2 = range(1,11)
mult_table = [[i*j for j in numbers1] for i in numbers2]
mult_table_s = str(mult_table)
for num in mult_table:
    print("\n", num)