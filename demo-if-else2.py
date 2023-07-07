# 1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# sayi = int(input('Bir sayı giriniz: ')) 
# if ((sayi > 0) and (sayi <= 100)):
#  print(f'Girdiğiniz sayı 0-100 aralığındadır.')
# else:
#  print(f'Girdiğiniz sayı 0-100 aralığında değildir.')


# 2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi = int(input('Bir sayı giriniz: '))
# if ((sayi > 0) and (sayi % 2 == 0)):
#    print(f'Girdiğiniz sayı pozitif çift sayıdır.')
# else:
#    print(f'Girdiğiniz sayı pozitif çift sayı değildir.')   


# 3-Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# if (girilenEmail == email):
#     if (girilenPassword == password):
#         print(f'Email ve Password doğru.')
#     else:
#         print(f'Password yanlış.')    
# else:
#     print(f'Email yanlış.')  


# 4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a > b) and (a > c):
#     print(f'a en büyük sayıdır')
# elif (b > a) and (b > c):
#     print(f'b en büyük sayıdır.')
# elif (c > b) and (c > a):
#     print(f'c en büyük sayıdır.')


# 5-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#   a-) Ortalama 50 olsa bile final ve notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input('vize1: '))
# vize2 = float(input('vize2: '))
# final = float(input('final: '))

# ortalama = ((vize1+vize2/2)*0.6 + (final * 0.4))

# if (ortalama >= 50):
#     print(f'Geçti')
# elif (ortalama >= 50) and (final >= 50):
#       print(f'Geçti')
# elif (final >= 70):
#      print(f'Geçti')
# else:
#     print(f'Kaldı')


# 6-Kişinin ad, kilo ve boy bilgilerini alıp kilo boy indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi) 
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#  0-18.4     => zayıf
#  18.5-24.9  => normal
#  25.0-29.9  => kilolu
#  30.0_34.9  => şişman(obez)

# name = input('adınız: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))

# index = (kg) / (hg ** 2)

# if (index >= 0) and  (index <= 18.4):
#   print(f'{name} kilo indexin: {index} ve kilo değerlendirmen zayif')
# elif (index > 18.4 ) and (index <= 24.9):
#   print(f'{name} kilo indexin: {index} ve kilo değerlendirmen normal')
# elif (index > 24.9 ) and (index <= 29.9):
#   print(f'{name} kilo indexin: {index} ve kilo değerlendirmen kilolu')
# elif (index > 29.9 ) and (index <= 34.9):
#   print(f'{name} kilo indexin: {index} ve kilo değerlendirmen obez')
# else:
#   print(f'Bilgileriniz yanlış.')

