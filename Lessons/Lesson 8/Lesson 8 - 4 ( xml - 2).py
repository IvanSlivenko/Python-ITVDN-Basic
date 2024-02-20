from xml.etree import ElementTree

data = ElementTree.Element('data')#------------------------------Створюємо перший тег data
items = ElementTree.SubElement(data, 'items')#-------------------------Створюємо підтег items

item1 = ElementTree.SubElement(items,'item')#-------------Створюємо підтеги item для підтегу items
item2 = ElementTree.SubElement(items,'item')#--

item1.set('name','item1')#------------------
item2.set('name','item2')#--

item1.text = 'item1abc'#---------------------------
item2.text = 'item2abc'#--


my_data = ElementTree.tostring(data)
with open ('../../Files/items_2.xml','wb') as my_file:
    my_file.write(my_data)


