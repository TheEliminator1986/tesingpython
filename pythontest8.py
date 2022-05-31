creatures = {
    "cat": "meow",
    "dog": "bow-wow",
    "fish": "glug",
}
def new_life(dictionary, animal, sound):
    dictionary[animal] = sound
    return dictionary
new_dictionary = new_life(dictionary = creatures, animal = "dog", sound = "bark")
print(new_dictionary)