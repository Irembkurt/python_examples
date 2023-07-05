x = 6
5 < x < 10

# and operatörü
result = (x > 5) and (x < 10)     # x>5 ve x<10 ikisi de doğruysa true, biri veya ikisi de yanlışsa false gelir.

# or operatörü
result = (x > 0) or (x % 2 == 0)   # True gelmesi için birinin doğru olması yeterli

# not operatörü
result = not(x > 0)              # bilginin tam tersini alıyor. 

print(result)