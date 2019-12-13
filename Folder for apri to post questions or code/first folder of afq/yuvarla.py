#Tam değer fonksiyonu.          // Full value function.

def yuvarla(a):
  '''Rounds down to an integer'''
  #a = float(input("a.bc sayısı girin\n")) // a = float (input ("enter a.bc number \ n"))

  if a % 1 != 0:
    a = a - (a % 1)
  #print(int(a))
  return int(a)
