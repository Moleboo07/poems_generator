## Créer les bases de données de mots pour les différentes sagas

import spacy
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import pandas as pd

# Charger le modèle et télécharger la liste de mots en français
nlp = spacy.load("fr_core_news_sm")
nltk.download('words')
nltk.download('punkt')
french_words = set(nltk.corpus.words.words())

# Créer la base de données de mots pour chaque saga
def create_db(text, data):
    sentences = sent_tokenize(text, language='french')
    for sentence in sentences:
        words = word_tokenize(sentence, language='french')
        data.extend(words)

# Associer le type (nom, adjectif...etc) et le genre à chaque mot des extraits.
def type(db):
    associations = {'Mot': [], 'Type': []}
    for word in db:
        doc = nlp(word)
        # Type
        word_type = doc[0].pos_
        #Création du dictionnaire
        associations['Mot'].append(word)
        associations['Type'].append(word_type)
    return associations


# Texte
db = []
extract_potter = """
Gryffondor :
La maison Gryffondor, fondée par Godric Gryffondor lui-même, est réputée pour ses valeurs de courage, de bravoure et d'audace. Les élèves de Gryffondor sont sélectionnés en fonction de leur intrépidité et de leur esprit aventureux. Le blason de la maison arbore un lion, symbole de la force et de la noblesse. Gryffondor est également connue pour sa salle commune chaleureuse située dans la tour ouest du château, avec des fauteuils confortables et une cheminée accueillante.

Serpentard :
Fondée par Salazar Serpentard, la maison Serpentard est connue pour ses caractéristiques de ruse, d'ambition et de détermination. Les élèves de Serpentard sont choisis pour leur ingéniosité et leur désir de réussite. Le blason de la maison arbore un serpent, symbole de la ruse et de la sagesse. La salle commune de Serpentard est située dans les cachots du château et est réputée pour son atmosphère mystérieuse et ses couleurs vert et argent.

Poufsouffle :
Helga Poufsouffle a fondé la maison Poufsouffle avec des valeurs de loyauté, de travail acharné et de justice. Les élèves de Poufsouffle sont sélectionnés pour leur sens de l'équité et leur travail acharné. Le blason de la maison arbore un blaireau, symbole de la détermination et de la persévérance. La salle commune de Poufsouffle est située près des cuisines du château et est réputée pour son ambiance chaleureuse et accueillante.

Serdaigle :
Rowena Serdaigle a créé la maison Serdaigle en mettant l'accent sur l'intelligence, la sagesse et la créativité. Les élèves de Serdaigle sont choisis pour leur esprit analytique et leur curiosité intellectuelle. Le blason de la maison arbore un aigle, symbole de la sagesse et de la clairvoyance. La salle commune de Serdaigle est située dans une tour élevée du château, offrant une vue panoramique sur les environs.
"""

extract_lotr = """
Legolas (Elfe) :
Legolas, fils du roi Thranduil du Royaume des Bois, est un elfe du peuple des Sindar. Ses yeux perçants témoignent de la clarté de la vision elfique, capable de distinguer des mouvements imperceptibles. Gracieux et agile, Legolas excelle dans l'art de l'archerie elfique, maniant son arc avec une précision exceptionnelle. Ses oreilles pointues reflètent son lien étroit avec la nature, et il possède une longévité qui le distingue des mortels. En tant que membre de la Communauté de l'Anneau, Legolas apporte son habileté au combat, son calme et sa sagesse elfique.

Gimli (Nain) :
Gimli, fils de Glóin, représente la fierté et la vaillance des nains. De petite taille mais robuste, Gimli est doté d'une force impressionnante et d'une résistance exceptionnelle. Son épaisse barbe et sa chevelure ébouriffée sont caractéristiques des nains, tout comme son amour pour les bijoux et les trésors souterrains. Armé d'une hache à double tranchant, Gimli excelle dans le combat rapproché et ne recule devant aucun défi. Son esprit intrépide et sa loyauté inébranlable en font un compagnon de confiance au sein de la Communauté.

Azog (Orc) :
Azog, le Roi des Gobelins de la Moria, est un redoutable orc qui incarne la cruauté et la brutalité de sa race. Sa peau sombre et ses crocs saillants accentuent son apparence terrifiante. Azog est connu pour sa force surhumaine et sa férocité au combat. Une cicatrice profonde traverse son visage, résultat d'un affrontement passé avec Thorin Écu-de-Chêne. En tant que leader des Gobelins, Azog est implacable dans sa quête de domination et représente la menace constante des ténèbres pour la Terre du Milieu.
"""

extract_starwars = """
JarJar Binks :
JarJar Binks, un Gungan originaire de la planète Naboo, est un personnage unique par son excentricité et son maladresse. Doté d'oreilles longues et d'une apparence amphibie, Jar Jar a une démarche maladroite qui contraste avec sa personnalité joyeuse. Bien qu'il soit souvent considéré comme comique, Jar Jar joue un rôle crucial dans la lutte contre l'Empire, s'associant aux Jedi et aux Rebelles pour combattre l'oppression. Sa nature optimiste et son innocence cachent une volonté inattendue et une loyauté indéfectible envers ses amis.

Yoda :
Maître Yoda, le sage et puissant maître Jedi, est l'une des figures les plus emblématiques de l'ordre Jedi. Malgré sa petite taille, Yoda possède une sagesse profonde et une maîtrise exceptionnelle de la Force. Son apparence centenaire et ses oreilles pointues sont caractéristiques de sa race mystérieuse. Yoda incarne les principes de l'équilibre et de la spiritualité Jedi, dispensant des enseignements inestimables à plusieurs générations de padawans. Sa voix unique et ses expressions énigmatiques ajoutent à son charme indéniable.

Dark Vador :
Autrefois Anakin Skywalker, le héros Jedi prometteur, Dark Vador est devenu l'incarnation du côté obscur de la Force. Son imposante armure noire et sa respiration mécanique créent une présence intimidante. La cape flottante ajoute à son aura de menace. La cicatrice sur son visage rappelle son passage du côté obscur. Dark Vador est à la fois un guerrier redoutable et un personnage tragique, hanté par ses choix passés. Son rôle en tant qu'apprenti de l'Empereur Palpatine le place au cœur du conflit galactique.
"""

# Exécution
create_db(extract_starwars, db)
associations = type(db)

# Créer un DataFrame à partir des résultats
df = pd.DataFrame(associations)

# Afficher le DataFrame
print(df)

df.to_csv("df_starwars.csv", index=False)