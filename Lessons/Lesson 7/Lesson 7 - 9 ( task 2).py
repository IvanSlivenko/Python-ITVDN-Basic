import collections
import itertools

string = "blue car is parked right behind the blue building with wals and red door"

def get_max_count_word(count_dict):
    max_count = 0
    max_count_word = None
    # print('count_dict.items()', count_dict.items())

    for word, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_count_word = word
    return max_count_word
    # return (fr"слово -- {max_count_word} -- зустрічається у тексті : --{max_count} -- разів")

def get_max_count_word_combinations(words, max_count_word):
    combinations = itertools.combinations(words,2)
    max_count_word_combinations = [comb for comb in combinations if max_count_word in comb]
    return max_count_word_combinations

def process(text):
    words = text.split(' ') #-------------------------- Перетворюємо строку на список зі слів
    # print('words :', words)
    counts = collections.Counter(words) #-------------- Створюємо словник, де ключ - це слово, а значення ключа - це кількість слів у речені
    # print('counts :', counts)
    max_count_word = get_max_count_word(counts) #----------- Рахуємо максимальну кількість разів, які зустрічається кожне слово
    max_count_word_combinations = get_max_count_word_combinations(words, max_count_word)
    # return max_count_words
    return max_count_word_combinations

rc = process(string)
print(rc)

