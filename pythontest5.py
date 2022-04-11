list_to_be_determined = []
def total(nice, focus, **drive):
    list_to_be_determined.append(nice)
    list_to_be_determined.append(focus)
    for time in drive.values():
        list_to_be_determined.append(time)
    print(list_to_be_determined)
total(nice = "Great", focus = "job", drive = "Alton")        