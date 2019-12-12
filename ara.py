# Recursive çift yönlü arama fonksiyonu

# d: kullanıcı tanımlı dizi
# n: eleman sayısı
# search: aranan değer
# median: dizi medyanı
# min: dizinin en küçük elemanı
# max: dizinin en büyük elemanı 
# n_ortanca = dizinin ortanca elemanının numarası

import yuvarla

def arama(d, n, search, n_min, n_max):    

    median = (d[n_max] + d[n_min]) / 2
    yuvarla.yuvarla(median)

    control = 0

    n = (n_max + n_min) / 2
    n_ortanca = n/2
    yuvarla.yuvarla(n_ortanca)

    if search < median:
        for i in range(n_min, n_ortanca, 1):
            if d[i] == search:
                control = 1
                return i
    
        return arama(d, n, search, median, n_max)
    
    elif search >= median:
        for i in range(n_max, n_ortanca,  -1):
            if d[i] == search:
                control = 1
                return i
        
        return arama(d, n, search, n_min, median)
    
    if control == 0:
        return 0 
    
