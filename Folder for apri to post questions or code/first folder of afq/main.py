import yuvarla
import sirala
import ara

n = int(input("dizi eleman sayısı;\n"))
# n = int (input ("number of array elements; \ n"))

# Diziye eleman eklenir;
# Add elements to the array;
dizi = []
for i in range(0, n, 1):
    print("-----------------------", i+1, ". elemanı girin:")
    dizi.append(int(input()))

print("\n")
sirala.sirala(dizi, n)

n_max = n-1
n_min = 0

print("-----------------\n-----------------")
search = int(input("Aranan sayıyı girin:\n"))
# search = int (input ("Enter the number searched: \ n"))

# Recursive arama fonksiyonu çağrılır:

sonuc = ara.arama(dizi, n, search, n_min, n_max)
if sonuc == "0":
    print("Aranan sayı dizide bulunamadı.")
    # print ("The number searched could not be found in the array.")
else:
    print("Aranan sayı girilen dizinin", sonuc, ". elemanı.")
    # print ("The dialed number is the result of the entered directory", input ,". element.")


