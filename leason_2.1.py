animal_color = {
    "dog": "yellow",
    "cat": "white",
    "bunny": "pink"
}
print(animal_color["dog"])

animal_color["dragon"] = "green"
print(animal_color)

animal_color["dog"] = "black"
print(animal_color)

del animal_color["cat"]
print(animal_color)