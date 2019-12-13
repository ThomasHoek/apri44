import yuvarla

def search(d, x, first, last):

    middle = (first + last) / 2            # takes the middle of first and last
    yuvarla.yuvarla(middle)              # makes an integer from it

    if x < middle:                      # if x is smaller then the middle of array d
        search(d, x, first, middle)        # recursive split the list in two on ortanca
    
    elif x > middle:
        search(d, x, middle, last)
    
    else:
        pass