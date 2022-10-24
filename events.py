from rich.console import Console
from event import Event
from rich.prompt import Prompt

import random
import os
import re

class Events():

    def __init__(self):
        self.COLORS = ("red", "blue", "yellow", "green")
        self.DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.console = Console()

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

        day = input("Choose a day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").title()
        if day not in self.DAYS:
            input(f"{day} is not a valid day. Press any key to continue....")
            return

        time = Prompt.ask("Hour (0-23)")
        try:
            time = int(time)
            if not 0 <= time < 24:
                input(f"{time} is not a valid hour. Press any key to continue....")
                return
        except:
            input(f"{time} is not a valid ID. Press any key to continue....")

        title = Prompt.ask("Title")
        event = Event((day, time), len(self.events), title, random.choice(self.COLORS))
        self.events.append(event)

    def del_event(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        input("You will be deleting an event. Press any key to continue....")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            self.console.print("Below are the current events: ")
            for event in self.events:
                info = event.get_info()
                title = info["title"]
                self.console.print(f" - ID {info['id']} : {title} : {info['date'][0]} at {info['date'][1]}")

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
        input("You will be editing an event. Press any key to continue....")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            self.console.print("Below are the current events: ")
            for event in self.events:
                info = event.get_info()
                title = info["title"]
                self.console.print(f" - ID {info['id']} : {title} : {info['date'][0]} at {info['date'][1]}")

            event_id = int(input("ID of the event to edit (-1 to abort): "))
            if event_id == -1:
                break

            value_to_edit = input("What do you want to edit [Title, Hour, Day]? ").lower()

            if value_to_edit == "title":
                new_title = input("Please provide a new title: ")
                self.events[event_id].set_title(new_title)
                break

            elif value_to_edit == "hour":
                new_time = int(input("Please provide a new hour (0-23): "))
                try:
                    new_time = int(new_time)
                    if not 0 <= new_time < 24:
                        input(f"{new_time} is not a valid hour. Press any key to continue....")
                        return
                except:
                    input(f"{new_time} is not a valid ID. Press any key to continue....")

                event = self.events[event_id]
                info = event.get_info()
                event.set_date((info["date"][0], new_time))
                break

            elif value_to_edit == "day":
                new_day = input("Please provide a new day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").title()
                if new_day not in self.DAYS:
                    input(f"{new_day} is not a valid day. Press any key to continue....")
                    return

                event = self.events[event_id]
                info = event.get_info()
                event.set_date((new_day, info["date"][1]))
                break
