from nltk.stem.snowball import RussianStemmer

f = open('water_words.txt')
water_words = []
while True:
    word = f.readline().strip()
    if word == '':
        break
    water_words.append(word)

symbols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—', '?', '=', '==',
                    '  ', '–']

predlogs = ["без", "безо", "близ", "в", "во", "вместо", "вне", "для",
            "до", "за", "из", "изо", "из-за", "из-под", "к", "ко",
            "кроме", "между", "меж", "на", "над", "надо", "о", "об", "обо",
            "от", "ото", "перед", "передо", "пред", "предо", "по", "под",
            "подо", "при", "ради", "про", "с", "со", "сквозь", "среди", "у",
            "чрез", "через"]

#text = "Написание текстов для главных страниц сайта – дело непростое. Проблема в том, что существует сразу несколько подходов к подготовке таких материалов. Каждый подход, как это и водится, имеет свои плюсы и минусы. Где-то можно выиграть в оптимизации, но потерять в живых читателях. Где-то можно приобрести живых читателей, но придется жертвовать SEO-показателями и, возможно, по этой причине отставать от конкурентов. Постоянные сомнения, касающиеся оптимальных путей создания текстов для главной, стали вполне привычными спутниками авторов. Кто-то постоянно работает под одной и той же схеме, кто-то мечется между SEO и продающими текстами, а кто-то и вовсе не имеет четкого видения. Чтобы хоть как-то определиться с тем, как писать тексты для главных страниц, мы составили эту небольшую заметку. На полноценный научный труд претендовать не собираемся, но кое-какие собственные наблюдения озвучим."

def count_symbols(text):
    return len(text)

def count_words(text):
    k = 0
    for i in text.split(' '):
        if i != '':
            k += 1
    return k

def key_words(text):
    global water_words
    global symbols

    stemmer = RussianStemmer()
    c = dict()
    returning_c = []

    for word in text.split(' '):
        try:
            if word[-1] in symbols:
                word = word.replace(word[-1], '')
        except:
            continue
        word = word.lower()
        if word in water_words or word in predlogs:
            continue
        word_var = stemmer.stem(word)
        b = c.get(word_var, [0])
        b[0] += 1
        if not word in b:
            b.append(word)
        c[word_var] = b

    sorted_c = dict(sorted(c.items(), key=lambda item: item[-1]))

    for k in range(50):
        try:
            x = sorted_c.popitem()
        except:
            break
        if x[1][0] == 1:
            break
        returning_c.append(x)

    return returning_c

def spam(text_words, key_words):
    k = 0
    for i in key_words:
        k += i[1][0]
    return k/text_words*100

def water(text, words):
    global water_words
    global symbols
    k = 0
    
    for i in text.split(' '):
        try:
            if i[-1] in symbols or i[0] == '\n':
                i = i.replace(i[-1], '')
        except:
            continue
        i = i.lower()
        if i in water_words:
            k += 1

    return k/words*100