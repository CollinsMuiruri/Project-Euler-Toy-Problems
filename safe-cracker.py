# When given a specific word, this function obtains all possibilities of the word
# in an order which starts from first letters eg: AAAA;
# By giving the number equal to repeat, the function will give the length of the
# string by the number given.
# It then breaks when the specified word is found.
# However, it will also give all combinations of a word if a "break" word is not given.

from itertools import product
import emoji


# check permutations until we find the word 'crack'
for x in product('ARCK', repeat=5):
    w = ''.join(x)
    print(w)
    if w.lower() == 'crack': break
    print(emoji.emojize(':+1:', use_aliases=True))
