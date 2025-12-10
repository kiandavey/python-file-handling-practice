import json

hero_profile = {
        "name" : "Aragon",
        "level" : 10,
        "is_alive" : True,
        "attributes" : {"strength" : 15, "magic" : 5},
        "inventory" : ["Sword", "Potion", "Map"]
    }

with open("hero.json", "w") as file:
    json.dump(hero_profile, file, indent=4)

with open("hero.json", "r") as file:
    loaded_hero = json.load(file)
    loaded_hero["level"] += 1
    loaded_hero["inventory"].append("Shield")
print(f"Welcome back, {loaded_hero['name']}!")
print(f"Current Level: {loaded_hero['level']}")
print(f"Current Inventory: {loaded_hero['inventory']}")