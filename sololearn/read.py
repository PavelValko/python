file = open('books.txt', 'r')

for line in file.readlines():
    short = ''
    for i in line.split():
        short += i[0]
    print(short)

file.close()


# file = open('books.txt', 'r')
#
# for line in file.readlines():
#     print(line[0] + str(len(line.strip())))
#
#
# file.close()