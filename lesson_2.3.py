animal_color = {
    "dog": "yellow",
    "cat": {
      "eyes": "brown",
      "hair": "black",
      "leg": "long"
    },
    "bunny": ["white", "pink", "blue"]
}

print(animal_color["cat"]["leg"])

for bunny_color in animal_color["bunny"]:
    print(bunny_color)