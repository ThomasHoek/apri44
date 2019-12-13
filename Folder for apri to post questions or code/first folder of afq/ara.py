# Recursive çift yönlü arama fonksiyonu                  // Recursive bidirectional search function

# d: kullanıcı tanımlı dizi                              // d: user defined array
# n: eleman sayısı                                       // n: number of elements
# search: aranan değer                                   // search: searched value
# median: dizi medyanı                                   // median: array median
# min: dizinin en küçük elemanı                          // min: The smallest element in the array
# max: dizinin en büyük elemanı                          // max: largest element of array
# n_ortanca = dizinin ortanca elemanının numarası        // n_ortanca = number of the median element of the array

import yuvarla

def arama(
        d :"user defined array",
        n: "number of elements in array",
        search: "searched value in array",
        n_min: "the smallest element in the array",
        n_max: "the largest element in the array"
        ):    
    '''bidirectional Recursive finds a number in an array '''

    median = (d[n_max] + d[n_min]) / 2          # takes median
    median = yuvarla.yuvarla(median)             # rounds median down

    control = 0

    n = (n_max + n_min) / 2                     # finds the middle of the array
    n_ortanca = n/2                             # find the number of the median element
    n_ortanca = yuvarla.yuvarla(n_ortanca)      # rounds the number down

    if search > median:                         # if the number to search for is smaller then the median
        for i in range(n_min, n_ortanca, 1):    # takes the first half of the list
            if d[i] == search:                  # if the number it searches for is in the first half, return it
                control = 1
                return i
    
        return arama(d, n, search, median, n_max)   # else recursive the last half
    
    elif search <= median:                      # if it is bigger
        for i in range(n_max, n_ortanca,  -1):  # searches in the last half
            if d[i] == search:                   # if it finds the number return it
                control = 1
                return i
        
        return arama(d, n, search, n_min, median)       # else resursive the first half
    
    if control == 0:                        # if the list is empty?
        return 0 


# d_inp = [1,2,3,4,5,6,7,8,9]
# n_inp = len(d_inp)
# search_inp = 3
# min_inp = min(d_inp)
# max_inp = max(d_inp) - 1 
# print(arama(d_inp,n_inp,search_inp,min_inp,max_inp))