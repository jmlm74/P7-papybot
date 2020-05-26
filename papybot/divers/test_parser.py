import json
import unicodedata


stop_words_minus = []
ponctuation = ['.', ',', '?', '!', '-', "'", '"', '[', ']']
list_mot_ok = []
ficstopwords = 'stopwords.txt'
ficperso = 'stopwordsperso.txt'
list_phrase = []
list_phrase2 = []


phrase = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?."

# Suppression ponctuation
for char in ponctuation:
    if char in phrase:
        phrase = phrase.replace(char, ' ')

print(phrase)
list_phrase = phrase.split()
for mot in list_phrase:
    try:
        mot = unicode(mot, 'utf-8')
    except (TypeError, NameError):
        pass
    mot = unicodedata.normalize('NFD', mot)
    mot = mot.encode('ascii', 'ignore')
    mot = mot.decode("utf-8")
    list_phrase2.append(mot.lower())


with open(ficstopwords, 'r') as f:
    stop_words = json.load(f)
with open(ficperso, 'r') as f:
    stop_words_perso = json.load(f)

stop_words.extend(stop_words_perso)

for t in stop_words:
    stop_words_minus.append(t.lower())

for mot in list_phrase2:
    if len(mot) > 0 and mot.lower() not in stop_words_minus:
        list_mot_ok.append(mot.lower())

print(list_mot_ok)
phrase = ' '.join(list_mot_ok)
print(phrase)
