#örnek1

isim = input('isminiz: ')
yas = int(input('yasiniz:'))
egitim = input('eğitim durumu: ')

if (yas >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
       print(f'{isim} ehliyet alabilirsin.')
    else:
       print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
else:
    print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')


