from win10toast import ToastNotifier
import time


toaster = ToastNotifier()

while True:
    toaster.show_toast(
        "💧 Drink Water Reminder",
        "It's time to drink a glass of water and stay hydrated!",
        duration=60,
        threaded=True
    )
    time.sleep(60) 
