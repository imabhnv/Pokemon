# Don't got confuse by the name of the file..Its just a name of a pokemon 😁
from bs4 import BeautifulSoup

with open('D:\PROGRAMMING LANGUAGES\PYTHON\PYTHON bs4\Pokemon\index2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

episode_tags = soup.find_all('h3', class_="style-scope ytd-rich-grid-media")

pokemon_journeys = []
pokemon_journeys_name = []

pokemon_the_series_xy = []
pokemon_the_series_xy_name = []

pokemon_master_journeys = []
pokemon_master_journeys_name = []

pokemon_ultimate_journeys = []
pokemon_ultimate_journeys_name = []

for episode_tag in episode_tags:
    title = episode_tag.find('a')["title"]
    
    episode_number = title 

    link = episode_tag.find('a')['href']
    if "Pokémon Journeys एपिसोड" in episode_number:
        pokemon_journeys.append(f"https://www.youtube.com/{link}")
        pokemon_journeys_name.append(episode_number)

    elif "Pokémon the Series: XY एपिसोड " in episode_number:
        pokemon_the_series_xy.append(f"https://www.youtube.com/{link}")
        pokemon_the_series_xy_name.append(episode_number)

    elif "Pokémon the Series: XY | एपिसोड " in episode_number:
        pokemon_the_series_xy.append(f"https://www.youtube.com/{link}")
        pokemon_the_series_xy_name.append(episode_number)

    elif "Pokémon Master Journeys एपिसोड " in episode_number:
        pokemon_master_journeys.append(f"https://www.youtube.com/{link}")
        pokemon_master_journeys_name.append(episode_number)

    elif "Pokémon Master Journeys | एपिसोड " in episode_number:
        pokemon_master_journeys.append(f"https://www.youtube.com/{link}")
        pokemon_master_journeys_name.append(episode_number)

    elif "Pokémon Ultimate Journeys | एपिसोड " in episode_number:
        pokemon_ultimate_journeys.append(f"https://www.youtube.com/{link}")
        pokemon_ultimate_journeys_name.append(episode_number)

print("Pokemon Journeys\n")
for i,j in zip(pokemon_journeys,pokemon_journeys_name):
    print(j)
    print(i)

print("\nPokemon The Series: XY\n")
for i,j in zip(pokemon_the_series_xy,pokemon_the_series_xy_name):
    print(j)
    print(i)

print("\nPokemon Master Journeys\n")
for i,j in zip(pokemon_master_journeys,pokemon_master_journeys_name):
    print(j)
    print(i)

print("\nPokemon Ultimate Journeys\n")
for i,j in zip(pokemon_ultimate_journeys,pokemon_ultimate_journeys_name):
    print(j)
    print(i)
