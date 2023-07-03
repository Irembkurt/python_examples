# Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. ( r: 3.14 )
# Daire Alanı : πr2      Daire Çevresi : 2πr

pi = 3.14

r = float(input("yarı çap: "))
 
alan = pi * ( r ** 2 )
cevre = 2 * pi * r 

print("alan" , alan)
print("cevre" , cevre)
