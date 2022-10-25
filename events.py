from rich.console import Console
from event import Event
from rich.prompt import Prompt

import random
import os
import re

class Events():

    def __init__(self):
        # Set constants
        self.COLORS = ("red", "blue", "yellow", "green")
        self.DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Create Rich console object
        self.console = Console()

        # Create starting events
        event1 = Event(("Tuesday", 10), 0, "Event 1")
        event2 = Event(("Sunday", 7), 1, "Event 2", "red")
        event3 = Event(("Friday", 8), 2, "Event 3", "yellow")
        event4 = Event(("Saturday", 8), 3, "Event 4", "blue")
        event5 = Event(("Monday", 8), 4, "Event 5", "blue")

        # Add events to a list
        self.events = [event1, event2, event3, event4, event5]

    def get_events(self):
        return self.events

    def add_event(self):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Input used to clear any previous keyboard input
        input("You will be creating a new event. Press any key to continue....")
        os.system('cls' if os.name == 'nt' else 'clear')

        # Get day
        day = input("Choose a day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").title()
        if day not in self.DAYS:
            # Return to Schedule if day is not valid
            input(f"{day} is not a valid day. Press any key to continue....")
            return

        # Get time
        time = Prompt.ask("Hour (0-23)")
        try:
            time = int(time)
            if not 0 <= time < 24:
                # Return to Schedule if time does not follow 24h system 
                input(f"{time} is not a valid hour. Press any key to continue....")
                return
        except:
            # Return to Schedule if time is not valid (not int, etc..)
            input(f"{time} is not a valid ID. Press any key to continue....")

        # Get title
        title = Prompt.ask("Title")
        # Instantiate an event
        event = Event((day, time), len(self.events), title, random.choice(self.COLORS))
        # Add the event to the list
        self.events.append(event)

    def del_event(self):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Input used to clear any previous keyboard input
        input("You will be deleting an event. Press any key to continue....")

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            # Inform user of current events
            self.console.print("Below are the current events: ")
            for event in self.events:
                info = event.get_info()
                title = info["title"]
                self.console.print(f" - ID {info['id']} : {title} : {info['date'][0]} at {info['date'][1]}")

            # Get the to-be deleted event's ID
            event_id = int(input("ID of the event to delete (-1 to abort): "))
            if event_id == -1:
                break
            try:
                del self.events[event_id]
                break
            except:
                # Return to Schedule if ID is not valid
                input(f"{event_id} is not a valid ID. Press any key to continue....")
                break


    def edit_event(self):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Input used to clear any previous keyboard input
        input("You will be editing an event. Press any key to continue....")

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            # Inform user of current events
            self.console.print("Below are the current events: ")
            for event in self.events:
                info = event.get_info()
                title = info["title"]
                self.console.print(f" - ID {info['id']} : {title} : {info['date'][0]} at {info['date'][1]}")

            # Get the to-be deleted event's ID
            event_id = int(input("ID of the event to edit (-1 to abort): "))
            if event_id == -1:
                break

            # The event's value to edit
            value_to_edit = input("What do you want to edit [Title, Hour, Day]? ").lower()

            # Get the new title and update the event 
            if value_to_edit == "title":
                new_title = input("Please provide a new title: ")
                self.events[event_id].set_title(new_title)
                break

            # Get the new time and update the event 
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

            # Get the new day and update the event 
            elif value_to_edit == "day":
                new_day = input("Please provide a new day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ").title()
                if new_day not in self.DAYS:
                    input(f"{new_day} is not a valid day. Press any key to continue....")
                    return

                event = self.events[event_id]
                info = event.get_info()
                event.set_date((new_day, info["date"][1]))
                break
