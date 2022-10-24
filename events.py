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

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = input("Choose a day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").title()
        if day not in days:
            input(f"{day} is not a valid day. Press any key to continue....")
            return

        time = int(Prompt.ask("Hour (0-23)"))
        if not 0 <= time < 24:
            input(f"{time} is not a valid hour. Press any key to continue....")
            return

        title = Prompt.ask("Title")
        event = Event((day, time), len(self.events), title, random.choice(self.COLORS))
        self.events.append(event)

    def del_event(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("You will be deleting an event. Press any key to continue....")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            event_id = int(input("ID of the event to delete (-1 to abort): "))
            if event_id == -1:
                break
            try:
                del self.events[event_id]
                break
            except:
                input(f"{event_id} is not a valid ID. Press any key to continue....")
                break


    def edit_event(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("You will be deleting an event. Press any key to continue....")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            event_id = int(input("ID of the event to edit (-1 to abort): "))
            if event_id == -1:
                break
            try:
                del self.events[event_id]
                break
            except:
                input(f"{event_id} is not a valid ID. Press any key to continue....")
                break
