#Dizi elemanlarını küçükten büyüğe sıralayan fonksiyon.

def sirala(x, n):
    
    for j in range(0, n, 1):
        for i in range(0, n-1, 1):
            if x[i] > x[i+1]:
                yedek = x[i]
                x[i] = x[i+1]
                x[i+1] = yedek  

    for i in range(0, n, 1):
        print(x[i], flush = True)
