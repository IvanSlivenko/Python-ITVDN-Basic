import re

text = "Hi @mr_lex ! My name  is John and love coffee.  #coffeeLover #2021"

print(text)

#-------------------------------------------------------------------------Пошук та заміна значень (перший параметр - що шукаємо,
# другий параметр - на що змінюємо,
# третій параметр - де шукаємо та змінюємо )
print(re.sub(r"[.!?\\-]",'', text))


#------------------------------------------------------------------------- Пошук елементів з хештегами
print([e for e in re.finditer(r"#[A-Aa-z0-9]*", text)])


#------------------------------------------------------------------------- Ділимо text по символам, що задані
#------------------------------------------------------------------------- у регулярних виразах
print(re.split(r"[.!?\\-]", text))

