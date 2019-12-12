import yuvarla
import sirala
import ara

n = int(input("dizi eleman sayısı;\n"))

# Diziye eleman eklenir;

dizi = []
for i in range(0, n, 1):
    print("-----------------------", i+1, ". elemanı girin:")
    dizi.append(int(input()))

print("\n")
sirala.sirala(dizi, n)

n_max = n
n_min = 0

print("-----------------\n-----------------")
search = int(input("Aranan sayıyı girin:\n"))

# Recursive arama fonksiyonu çağrılır:

sonuc = ara.arama(dizi, n, search, min, max)
if sonuc == "0":
    print("Aranan sayı dizide bulunamadı.")
else:
    print("Aranan sayı girilen dizinin", sonuc, ". elemanı.")


