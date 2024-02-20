from xml.dom import minidom

my_doc = minidom.parse('../../Files/items.xml') #--------------Читаємо файл

items = my_doc.getElementsByTagName('item')#------------------ Знаходимо потрібні теги

print(len(items))
print(items[0].attributes['name'].value)
print('-'*45)


for el in items:
    print(el.attributes['name'].value)

print('-'*45)