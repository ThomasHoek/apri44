import yuvarla

def search(d, x, first, last):

    ortanca = (first + last) / 2            # takes the middle of first and last
    yuvarla.yuvarla -(ortanca)              # makes an integer from it

    if x < d[ortanca]:                      # if x is smaller then the middle of array d
        search(d, x, first, ortanca)        # recursive split the list in two on ortanca

