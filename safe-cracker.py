# When given a specific word, this function obtains all possibilities of the word
# in an order
# which starts from first letters eg: AAAA;
# It then breaks when the specified word is found
# However, it will also give all combinations of a word if a "break" word is not given.

from itertools import product

# check permutations until we find the word 'crack'
for x in product('123', repeat=3):
    w = ''.join(x)
    print(w)
    if w.lower() == 'crack': break
