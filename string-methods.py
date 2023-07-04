message = ' Hello There. My name is Nil. '

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.strip()          #strip baştaki boşluk karakterini gideriyor.
# message = message.split()          #split cümleyi parçalara ayırır.
# message = ''.join(message)         #join elemanlar arası sembol ekleyerek birleştirir.Sembol eklemeden de olur.
# index = message.find('name')       #find cümle içinde istenilen bilgiyi bulur.
# print(index)                       #index cümle içerisinde bilgiyi arar. bilginin ilk harfindeki index numarasını söyler
# isFound = message.startswith('H')  #mesaj içerisindeki bilginin H ile mi başladığını sordum.
# print(isFound)
# isFound = message.endswith('l')    #mesaj içindeki bilginin l ile mi bittiğini sordum.
# print(isFound)
# message = message.replace('Nil','Beyza')   #Replace ile istediğim bilgiyi farklı bir bilgiyle değiştirdim.
message = message.center(100)          # center vermiş olduğumuz string bilgiyi 100 karakterlik bilgi içerisine yazar

print(message)