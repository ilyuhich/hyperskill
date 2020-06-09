# read animals.txt
# and write animals_new.txt
file = open("animals.txt", "r")
file_new = open("animals_new.txt", "w")
animals =[]
for line in file:
    animals.append(line.replace("\n", ""))
file_new.write(" ".join(animals))
file.close()
file_new.close()
