# 1-Girilen sayının 0-100 aralığında olup olmadığı.

# sayi = float(input('sayı: '))
# result = (sayi > 0) and (sayi < 100)
# print(f'sayı 0-100 arasında mı: {result}')


# 2-Girilen sayının pozitif çift sayı olup olmadığı.

# sayi = float(input('sayı: '))
# result = (sayi > 0) and (sayi % 2 == 0)
# print(f'sayının pozitif ve çift olma durumu: {result}')


# 3-Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'ibk@gmail.com'
# password = '12345'
# girilenEmail = input('email: ')
# girilenPassword = input('password: ')
# result = (girilenEmail == email) and (girilenPassword == password)
# print(result)


# 4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and (a > c)
# print(f'a en büyük sayıdır: {result}')

# result = (b > a) and (b > c)
# print(f'b en büyük sayıdır: {result}')

# result = (c > b) and (c > a)
# print(f'c en büyük sayıdır: {result}')


# 5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

# vize1 = float(input('vize1: '))
# vize2 = float(input('vize2: '))
# final = float(input('final: '))

# ortalama = ((vize1 + vize2 / 2 ) *0.6) and (final * 0.4)
# result = (ortalama>=50) and (final>=50)
# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {result}')


# 6-Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#  formül : (Kilo / boy uzunluğunun karesi)
#  aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#  0-18.4     => zayıf
#  18.5-24.9  => normal
#  25.0-29.9  => kilolu
#  30.0_34.9  => şişman(obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and  (index <= 18.4)
normal = (index > 18.4 ) and (index <= 24.9)
kilolu = (index > 24.9 ) and (index <= 29.9)
obez = (index > 29.9 ) and (index <= 34.9)

print(f'{name} kilo indexin: {index} ve kilo değerlendirmen zayif: {zayif}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indexin: {index} ve kilo değerlendirmen obez: {obez}')