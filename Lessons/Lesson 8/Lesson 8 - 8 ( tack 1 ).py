import random
letters = 'abcdefghijklmnoprstuwxyzq'
random_letters = ''
print(len(letters))

while len(random_letters)<25:
    random_letter = letters[random.randint(0,len(letters)-1)]
    print(random_letter)
    random_letters+=random_letter
print(random_letters)

with open('../../Files/random_string','w') as text_file: #---Відкриваємо файл для запису
    text_file.write(random_letters)#---Записуємо інформацію у файл



print('OK')



