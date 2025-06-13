import datetime
import time
from playsound import playsound

def get_alarm_time():
    while True:
        alarm_input = input("Set alarm time (HH:MM, 24-hour format): ")
        try:
            alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M").time()
            return alarm_time
        except ValueError:
            print("Invalid time format. Please try again.")

def main():
    print("==== Alarm Clock ====")
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time.strftime('%H:%M')}")

    while True:
        now = datetime.datetime.now().time().replace(second=0, microsecond=0)
        if now == alarm_time:
            print("⏰ Wake up! Alarm ringing!")
            playsound("alarm_sound.mp3")  # Ensure this file exists in the same folder
            break
        time.sleep(10)

if __name__ == "__main__":
    main()
  
