from event import Event
from rich.prompt import Prompt
import os
class Events():
    def __init__(self):
        # date is tuple: (day (M, TU, W, TH, F, SA, SU), hour)
        event1 = Event(("TU", 10), "Event 1")
        event2 = Event(("SU", 7), "Event 2", "red")
        event3 = Event(("F", 8), "Event 3", "yellow")
        event4 = Event(("SA", 8), "Event 4", "blue")
        event5 = Event(("M", 8), "Event 5", "blue")

        self.events = [event1, event2, event3, event4, event5]

    def get_events(self):
        return self.events

    def add_event(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        # day = Prompt.ask("Choose a day", choices=["Monday", "Tuesday", "Wednesday"])
        day = input("Choose a day [Monday, Tuesday, Wednesday]: ")
        day = day[1:]
        time = int(Prompt.ask("Hour (0-23)"))
        title = Prompt.ask("Title")
        event = Event(("M", time), title)
        self.events.append(event)

    def del_event(self):
        event = input("Del your event: \n")

    def edit_event(self):
        event = input("Edit your event: \n")
