import time

def countdown_timer(total_seconds):
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timeformat)
        time.sleep(1)
        total_seconds -= 1
    print('Time\'s up!')

def main():
    time_input = input("Enter the time to countdown (format: hours:minutes:seconds): ")
    try:
        hours, mins, secs = map(int, time_input.split(':'))
        total_seconds = hours * 3600 + mins * 60 + secs
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid time format")

if __name__ == "__main__":
    main()
