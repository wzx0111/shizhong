import time

def pomodoro_timer(minutes):
    """A function that starts a timer for a specified number of minutes."""
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(m, s)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    minutes = 25
    pomodoro_timer(minutes)
