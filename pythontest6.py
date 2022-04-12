def colors(primary_colors, nice_colors):
    for new_colors in primary_colors:
        if nice_colors == new_colors:
            print("good")
            break
goals = input("Enter a color:")
primary_colors = ("yellow", "red", "blue")
colors(primary_colors, goals)    