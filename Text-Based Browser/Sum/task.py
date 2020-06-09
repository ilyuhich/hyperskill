# read sums.txt
# сделал вычисление суммы чисел из файла в строках
f = open("sums.txt")
file_list = f.readlines()
for line in file_list:
    sums = 0
    line_num = line.split()
    for num in line_num:
        sums = sums + int(num)
    print(f"{sums}")
f.close()
