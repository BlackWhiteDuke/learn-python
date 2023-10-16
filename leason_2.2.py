animal_color = {
    "dog": "yellow",
    "cat": "white",
    "bunny": "pink"
}

for animal,color in animal_color.items():
    print(animal, "=", color)

for animal in animal_color.keys():
    print(animal, "=", animal_color[animal])

for color in animal_color.values():
    print(color)