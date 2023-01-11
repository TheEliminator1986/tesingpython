'''
Countdown Timer
-----------------------------------------------------------------
'''


import time


def new_count(new_time):
    while new_time >= 0:
        mins, secs = divmod(new_time, 60)
        new_timer = "{:02d} : {:02d}".format(mins, secs)
        print(new_timer, end="\r")
        time.sleep(1)
        new_time -= 1
    print("Lift off!")


if __name__ == "__main__":
    new_time = int(input("Enter a time in seconds: "))
    new_count(new_time)