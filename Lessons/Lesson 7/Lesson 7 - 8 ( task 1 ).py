import collections
string = "blue car is parked right behind the blue building with wals and red door"

def get_max_count_word(count_dict):
    max_count = 0
    max_count_word = None
    # print('count_dict.items()', count_dict.items())

    for word, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word
    # return max_count_word, max_count
    return (fr"слово -- {max_count_word} -- зустрічається у тексті : --{max_count} -- разів")
def process(text):
    words = text.split(' ') #-------------------------- Перетворюємо строку на список зі слів
    # print('words :', words)

    counts = collections.Counter(words) #-------------- Створюємо словник, де ключ - це слово,
                                        # а значення ключа - це кількість слів у речені

    # print('counts :', counts)


    max_count_word = get_max_count_word(counts) #----------- Рахуємо максимальну кількість разів, які зустрічається кожне слово

    return max_count_word

rc = process(string)
print(rc)

