# "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
listA = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(listA)

# Liste kaç elemanlıdır?
result = len(listA)

# listenin ilk ve son elemanı nedir ?
result = listA[0]
result = listA[3]

# Mazda değerini toyota ile değiştirin.
# listA[-1]= 'Toyota' 
# result = listA

# Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in listA

# Listenin -2 indexindeki değer nedir?
result = listA[-2]

# Listenin ilk 3 elemanını alalım.
result = listA[0:3]

# Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
listA[-2]= ['Toyota', 'Renault']
result = listA

# Listenin üzerine audi ve nissan değerlerini ekleyin.
result = listA + ['Audi', 'Nissan']

# Listenin son elemanını silin.
del listA[-1]
result = listA

# Liste elemanlarını tersten yazdırın.
result = listA[::-1]

# Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB = ['Sena', 'Turan', 1999, [80,80,70]]
studentC = ['Ahmet', 'Turan', 1998, [80,70,90]]

# Liste elemanlarını ekrana yazdırınız.
print(studentA + studentB + studentC)




print(result)