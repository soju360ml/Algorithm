from itertools import islice

source = [i for i in range(1, 11)]
for i in enumerate(islice(source, 3, None)):
    print(i, ' ', end='')