import sys

for index in range(1, len(sys.argv)):
    with open(sys.argv[index], 'r') as my_file:
        print(my_file.read(), end = '')
    my_file.close()