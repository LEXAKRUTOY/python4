import requests
import json
from random import randint as rnd

class RickAndMortyApi:
    BASE_URL = "https://rickandmortyapi.com/api/"
    
    def get_random_character(self):
        
        rnd_character = str(rnd(1,826))
        data = requests.get(f"{self.BASE_URL}character/{rnd_character}")
        
        json_data = json.dumps(data.json())
        return json.loads(json_data)
    
    def search_characters(self):
        
        name = input("Input id your character: ")
        data = requests.get(f"{self.BASE_URL}character/{name}")
        
        json_data = json.loads(data.json())
        return json.loads(json_data)
    
    def get_all_locations(self):
        data = requests.get(f"{self.BASE_URL}location/")
        
        json_data = json.dumps(data.json())
        json_p_data = json.loads(json_data)
        
        return json_p_data.get("results")
    
    def search_episodes(self):
        
        name = input("Input id your episod: ")
        data = requests.get(f"{self.BASE_URL}episode/{name}")
        
        json_data = json.dumps(data.json())
        return json.loads(json_data)
        
    def analyze_character_status(self):
        
        name = input("Input id your character: ")
        data = requests.get(f"https://rickandmortyapi.com/api/character/{name}")

        json_data = json.dumps(data.json())
        json_p_data = json.loads(json_data)

        status = json_p_data.get('status')

        return status

while True:
    choice = input("Hello! \n 1. Random character \n 2. Search character \n 3. All location\n 4. Search episodes \n 5. Analyze character status\nExit\nChoice: ")
    client = RickAndMortyApi()

    if choice == "1":
        random_character = client.get_random_character()
        print(f"Random character: {random_character['name']}")
        
    elif choice == "2":
        search_character = client.search_characters()
        print(f"Your character: {search_character['name']}")
        
    elif choice == "3":
        all_locations = client.get_all_locations()
        print("All locations:")
        for location in all_locations:
            print(f" - {location.get('name')}")
        
    elif choice == "4":
        search_episode = client.search_episodes()
        print(f"All locations: {search_episode['name']}")
        
    elif choice == "5":
        character_status = client.analyze_character_status()
        print(f"Status: {character_status}")
        
    elif choice == "Exit":
        break
    
    else:
        print("Input a number or Exit")