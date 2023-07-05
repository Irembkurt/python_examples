x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# a = int(input('1.sayı: '))
# b = int(input('2.sayı: '))

# result = (a * b) - (x+y+z)


# y nin x e kalansız bölümünü hesaplayınız.
result = y // x


# (x,y,z) toplamının mod 3ü nedir?
toplam = (x + y + z)
result = toplam % 3


# y nin x. kuvvetini hesaplayınız?
result = y ** x


#x, *y, z = numbers işlemine göre z nin küpü kaçtır?
x, *y ,z = numbers
result = z ** 3

#x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?
x, *y ,z = numbers
result = y[0] + y[1] + y[2]


print(result)