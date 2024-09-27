from django.shortcuts import render
from django.http import HttpResponse
import requests

class Pokemon:
    def __init__(self, name, type_, description, level):
        self.name = name
        self.type_ = type_
        self.description = description
        self.level = level

    def get_sprite(self):
        print(f'Getting sprite for {self.name}')
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name.lower()}')
        if response.status_code == 200:
            data = response.json()
            self.sprite_url = data['sprites']['front_default']
            print(self.sprite_url)
        else:
            self.sprite_url = 'Sprite not found'

# Create a list of Pokemon instances
pokemon = [
    Pokemon('Pikachu', 'electric', 'Loves to zap things.', 15),
    Pokemon('Bulbasaur', 'grass/poison', 'Has a plant bulb on its back.', 5),
    Pokemon('Charmander', 'fire', 'Spits fire from its tail.', 10),
    Pokemon('Squirtle', 'water', 'Shoots water from its mouth.', 8)
]

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the pokemons_index view
def pokemon_index(request):
    for poke in pokemon:
      print(poke.name)
      poke.get_sprite()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })
