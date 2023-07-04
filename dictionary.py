# key - value

# sehirler = ['kocaeli', 'istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('kocaeli')])

# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

# plakalar = { 'kocaeli' : 41, 'istanbul' : 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# print(plakalar)

users = {
    'sadikturan': {
        'age': 36,
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '12312312'
    },
    'cinarturan': {
        'age': 2,
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '12312312',
    }
}
print(users)