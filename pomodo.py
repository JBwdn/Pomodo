# Pomodoro timer - Jake Bowden 04/19
import time
P = 0
choices = ["p", "s", "l"]
mode = ""
while 1 > 0:
    print('Pomodoros this session:', P)
    # Collect timer setting:
    while mode not in choices:
        mode = str.lower(input('(P)omodoro/(S)hort/(L)ong?:'))
    # Set time:
    if mode == "p":
        t = 25
        P += 1
    elif mode == "s":
        t = 5
    elif mode == "l":
        t = 10
    # Reset and run timer:
    mins = 0
    while mins != t:
        print(mins + 1, end=" ", flush=True)
        time.sleep(60)
        mins += 1
    # Play sound:
    print("\a")
    mode = ""
