# <center> P7 - Papy-Robot  </center>  

# P7 du parcours DA Python d'OpenClassRoom

## Créez GrandPy Bot, le papy-robot 🤖 👴  

Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴  
Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?
Cahier des charges  
### Fonctionnalités
#### Interactions en AJAX  
L'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.  
 Vous utiliserez l'API de Google Maps et celle de Media Wiki.  
 Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.  
 Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !  
#### Parcours utilisateur  
L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :  
- header : logo et phrase d'accroche  
- zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.  
- footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez  

L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.  

Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.  

GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia](https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis).  


#### Étapes  
1 : Planifier son projet  
Découpez votre projet en étapes et sous-étapes en suivant une méthodologie de projet agile que vous adapterez à vos besoins. Remplissez un tableau Trello ou Pivotal Tracker.  
Avant de coder, initialisez un repo Github et faites votre premier push.  
2 : Initialiser Flask  
Créez un nouveau projet avec Flask, un framework Python très léger.  
Adoptez une approche Test Driven Development: commencez par écrire vos tests (qui seront rouges), puis votre code (vos tests seront alors verts) et refactorisez.  
3 : Interface Utilisateur  
Concevez le front-end du site en vous aidant de Bootstrap si vous le souhaitez. L'interface doit être responsive et consultable sur mobile !  
4 : Un parser de killer  
Comment allez-vous analyser la question qui est envoyée ? Tout simplement en la "parsant" (à prononcer "parssant"). Quel mot barbare ! "Parser" veut dire "découper un ensemble de données en petits ensembles manipulables séparément". En l'occurrence, vous découperez la phrase en mots que vous analyserez ensuite pour ne garder que les mots-clés (une adresse par exemple).  
Petite astuce : vous pouvez utiliser cette excellente base de stop words en français 🇫🇷
5 : Afficher les résultats de la recherche Google Maps  
Commencez par lire la documentation de l'API Google Maps pour l'initialiser dans votre projet. Puis intéressez-vous à la recherche : comment allez-vous interroger l'API pour la requête "Paris" par exemple ? Quel type de réponse recevrez-vous ? Sous quel format ?  
Utilisez cette réponse pour la formater à vos besoins et l'afficher dans votre page. Enfin, trouvez le moyen d'afficher une carte sous le message.  
Utilisez un mock pour tester cette nouvelle fonctionnalité.
6 : Père Castor, raconte-nous une histoire  
Développez la nouvelle fonctionnalité qui donne une âme à notre Papy Robot ! Vous allez récupérer les informations de Wikipedia correspondant à l’endroit recherché et afficher les premières lignes.
Pour cela, répétez l'étape 4 mais cette fois-ci en utilisant l'API Media Wiki. Vous pouvez également vous amuser en inventant plusieurs phrases différentes que GrandPy pourrait dire aléatoirement 🤓
7 : Mise en ligne 🚀  
Puis mettez en ligne votre belle application en utilisant Heroku.  

## Livrables  
### Principe  
 - Posez votre question à GrandPy en langage naturel.  
 - La question est parsée pour en ressortir les mots clés  
 - Les mots clés sont envoyés à l'API de GOOGLE MAP puis WIKIPEDIA pour trouver l'adresse du lieu et une petite histoire (3 1eres phrases de wikipedia). Si aucune donnée ne remonte de GOOGLE MAP le programme vous invite à reformuler votre question  
### Langages de developpement et outils  
 - python  
 - Flask  
 - Google Map  
 - Wikipedia  
 - OpenStreetMap (affichage Map)  
 - Pytest (tests unitaires)  
### Liens  
L'application est visible [ici](https://jmlm-p7papybot.herokuapp.com/).  
La documentation se trouve [à cet endroit](https://github.com/jmlm74/P7-papybot/tree/master/Doc).  

