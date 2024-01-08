## Générateur de poèmes basé sur les sagas

import cohere
import tiktoken
import openai
import os
from openai import OpenAI
import pandas as pd

client = OpenAI(api_key='votre_clé_API')

choix_film_user = None

#L'utilisateur choisit d'abord une sage parmi les trois proposées.
while choix_film_user not in ['Star_Wars', 'Harry_Potter', 'Seigneur_des_anneaux']:
    choix_film_user = input("Choisissez parmi Star_Wars, Harry_Potter ou Seigneur_des_anneaux : ")

    if choix_film_user not in ['Star_Wars', 'Harry_Potter', 'Seigneur_des_anneaux']:
        print("Choix invalide. Veuillez entrer une valeur parmi Star_Wars, Harry_Potter, Seigneur_des_anneaux. Respectez l'orthographe !")

#Une fois la saga choisie, il sélectionne un personnage de l'univers en question.
if choix_film_user == 'Star_Wars':
    perso_user = None
    while perso_user not in ['Jar_Jar_Binks', 'Yoda', 'Vador']:
      perso_user = input("Choisissez parmi Jar_Jar_Binks, Yoda ou Vador : ")

      if perso_user not in ['Jar_Jar_Binks', 'Yoda', 'Vador']:
          print("Choix invalide. Veuillez entrer un personnage valide parmi Jar_Jar_Binks, Yoda, Vador. Respectez l'orthographe !")


elif choix_film_user == 'Harry_Potter':
    perso_user = None
    while perso_user not in ['Gryffondor', 'Poufsouffle', 'Serdaigle', 'Serpentard']:
      perso_user = input("Choisissez parmi Gryffondor, Poufsouffle, Serdaigle ou Serpentard: ")

      if perso_user not in ['Gryffondor', 'Poufsouffle', 'Serdaigle', 'Serpentard']:
          print("Choix invalide. Veuillez entrer un personnage valide parmi Gryffondor, Poufsouffle, Serdaigle,Serpentard. Respectez l'orthographe !")


elif choix_film_user == 'Seigneur_des_anneaux':
    perso_user = None
    while perso_user not in ['Azog', 'Legolas', 'Gimli']:
      perso_user = input("Choisissez parmi Azog, Legolas ou Gimli : ")

      if perso_user not in ['Azog', 'Legolas', 'Gimli']:
          print("Choix invalide. Veuillez entrer un personnage valide parmi Azog, Legolas, Gimli. Respectez l'orthographe !")

#Pour finir, il choisit le type de poème qu'il souhaite.
choix_poem_user = None

while choix_poem_user not in ['Sonnet', 'Haiku', 'Ballade']:
    choix_poem_user = input("Choisissez parmi Sonnet, Haiku ou Ballade  : ")

    if choix_poem_user not in ['Sonnet', 'Haiku', 'Ballade']:
        print("Choix invalide. Veuillez entrer une valeur parmi Sonnet, Haiku, Ballade. Respectez l'orthographe !")

#On utilise les DataSets de mots afin de donner une personnalité à ChatGPT et des mots à utiliser.
#On télécharge les DataSets liés aux sagas.
data_lotr = './df_lotr.csv'
data_star_wars = './df_starwars.csv'
data_harry_potter = './df_potter.csv'

df_lotr = pd.read_csv(data_lotr)
df_star_wars = pd.read_csv(data_star_wars)
df_harry_potter = pd.read_csv(data_harry_potter)

if choix_film_user == 'Seigneur_des_anneaux':
    df_selected = df_lotr
elif choix_film_user == 'Star_Wars':
    df_selected = df_star_wars
elif choix_film_user == 'Harry_Potter':
    df_selected = df_harry_potter
else:
    print("Choix invalide")


#On convertit le dataframe en string pour qu'il puisse être lu par l'IA.
df_str = df_selected.to_string()

#On utilise l'API de ChatGPT comme générateur de poème en lui donnant les instructions sélectionnées précédemment.
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "tu es "+perso_user+" de l'univers de "+choix_film_user+" voici une liste de mot te concernant : "+df_str },
        {"role": "user","content": "fais moi un poème de type "+choix_poem_user+" en te comportant comme "+perso_user},
    ],
    model="gpt-3.5-turbo",
)

#On affiche le poème.
print("\n Voici votre poème:\n")
print(chat_completion.choices[0].message.content)