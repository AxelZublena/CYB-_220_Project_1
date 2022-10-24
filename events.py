from event import Event
from rich.prompt import Prompt

import random
import os

class Events():

    def __init__(self):
        self.COLORS = ("red", "blue", "yellow", "green")
        event1 = Event(("Tuesday", 10), 0, "Event 1")
        event2 = Event(("Sunday", 7), 1, "Event 2", "red")
        event3 = Event(("Friday", 8), 2, "Event 3", "yellow")
        event4 = Event(("Saturday", 8), 3, "Event 4", "blue")
        event5 = Event(("Monday", 8), 4, "Event 5", "blue")

        self.events = [event1, event2, event3, event4, event5]

    def get_events(self):
        return self.events

    def add_event(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("You will be creating a new event. Press any key to continue....")
        os.system('cls' if os.name == 'nt' else 'clear')

        day = input("Choose a day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
        time = int(Prompt.ask("Hour (0-23)"))
        title = Prompt.ask("Title")
        event = Event((day, time), len(self.events), title, random.choice(self.COLORS))
        self.events.append(event)

    def del_event(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("You will be creating deleting an event. Press any key to continue....")
        os.system('cls' if os.name == 'nt' else 'clear')

        event_id = input("ID of the event to delete: ")
        event_id = int(event_id[1:])
        del self.events[event_id]

    def edit_event(self):
        event = input("Edit your event: \n")
