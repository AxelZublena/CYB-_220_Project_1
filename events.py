from event import Event
from rich.prompt import Prompt

import random

class Events():

    def __init__(self):
        self.COLORS = ("red", "blue", "yellow", "green")
        event1 = Event(("Tuesday", 10), "Event 1")
        event2 = Event(("Sunday", 7), "Event 2", "red")
        event3 = Event(("Friday", 8), "Event 3", "yellow")
        event4 = Event(("Saturday", 8), "Event 4", "blue")
        event5 = Event(("Monday", 8), "Event 5", "blue")

        self.events = [event1, event2, event3, event4, event5]

    def get_events(self):
        return self.events

    def add_event(self):
        day = input("Choose a day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
        day = day[1:]
        time = int(Prompt.ask("Hour (0-23)"))
        title = Prompt.ask("Title")
        event = Event((day, time), title, random.choice(self.COLORS))
        self.events.append(event)

    def del_event(self):
        event = input("Del your event: \n")

    def edit_event(self):
        event = input("Edit your event: \n")
