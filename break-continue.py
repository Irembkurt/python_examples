# 1 den 100'e kadar tek sayıların toplamı.

x = 0
result = 0

while x <= 100:
    x +=1
    if x % 2 == 1:
        continue
    result += x
print(f'toplam: {result}')   