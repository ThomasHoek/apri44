#Dizi elemanlarını küçükten büyüğe sıralayan fonksiyon.
# Function to sort array elements from small to large.

def sirala(x, n):
    '''sorts an array'''     

    for j in range(0, n, 1):
        for i in range(0, n-1, 1):
            if x[i] > x[i+1]:
                yedek = x[i]            # yedek gets assigned as the current x
                x[i] = x[i+1]           # The current x gets replaced with the next x
                x[i+1] = yedek          # The next x gets replaced with yedek / the old current x
                
    for i in range(0, n, 1):
        print(x[i], flush = True)

