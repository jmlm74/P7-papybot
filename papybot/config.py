map_style = {
    'GOOGLE': False,
    'OSM': True,
}

MAPBOX = {
    'key': "pk.eyJ1Ijoiam1sbTc0IiwiYSI6ImNrYWpwbTFmZDBjdG4yeW1pN2hiajR2NGwifQ.kxwD_WKTvSXMiPtHkQV2HQ",
}

GOOGLE = {
    'key': "123456789",
    # 'url': "https://maps.googleapis.com/maps/api/geocode/json?address=",
    'url': "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&fields=name,geometry,formatted_address&input=",
}

WIKI = {
    'url1': "https://fr.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch=",
    'url2': "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&pageids=",
    'url3': "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&explaintext&exsentences=3&pageids=",
}

MESSAGES = [
    "Mais t\'ai-je déjà raconté l\'histoire de ce quartier qui m\'a vu en culottes courtes ?",
    "Voilà mon grand",
    "Ah attends un peu ! Ca me revient !",
    "Bien sûr mon petit ! Tu doutes de ton grand-père !",
    "Oh oui, je m'en souviens bien, ça tombe bien qu tu m\'en parles.",
    "Ouh, ça fait un bail! J'ai un peu perdu la mémoire tu sais !",
    "Oh, oui, je connais. D'ailleurs j'ai passé un boût de temps dans le coin.",
    "GrandMy adorait cet endroit, on y est allé souvent",
    "Ah avec ta grand-mère on y a passé de bons moments… ",
]
