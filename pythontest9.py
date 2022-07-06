super_heroes = {
    0: {
        "first name": "Luke",
        "last name": "Cage",
    },
    1: {
        "first name": "Jessica",
        "last name": "Knight",
    },
    2: {
        "first name": "Iron",
        "last name": "Fist",
    },
}
del super_heroes[0]
super_heroes[1]["last name"] = "Jones"
print(super_heroes)
