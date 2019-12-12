#Tam değer fonksiyonu.

def yuvarla(a):
  #a = float(input("a.bc sayısı girin\n"))

  if a % 1 != 0:
    a = a - (a % 1)
  #print(int(a))
  return int(a)

                                      