import datetime
from event import Event

from rich.table import Table
from rich.panel import Panel

class Schedule():
    def __init__(self, events):
        self.top_hour = 0
        self.week = [d for d in self.get_week(datetime.datetime.now().date())]
        self.events = events
        self.table = self.createTable()
        self.table_panel = Panel(self.table, style="")


    def get_panel(self):
        return self.table_panel

    def set_events(self, events):
        self.events = events

    def update(self, events):
        '''
        1. Re-create the table (schedule) 
        2. Loop through every hours (0-23)
        3. Create the row for every hours
        4. Update the pannel
        '''
        self.table = self.createTable()
        for hour in range(self.top_hour, 56):
            real_h = hour%24
            self.create_row(real_h, events)

        self.table_panel = Panel(self.table, style="")


    def createTable(self):
        '''Creates Rich table object with 7 columns (Hours and days)'''
        # Main window: schedule
        table = Table(show_header=True, header_style="bold blue", show_edge=False, expand=True, show_lines=True)
        table.add_column("Hours", style="dim", ratio=1)
        table.add_column(f"Monday ({self.week[0]})", style="dim", ratio=2)
        table.add_column(f"Tuesday ({self.week[1]})", style="dim", ratio=2)
        table.add_column(f"Wednesday ({self.week[2]})", style="dim", ratio=2)
        table.add_column(f"Thursday ({self.week[3]})", style="dim", ratio=2)
        table.add_column(f"Friday ({self.week[4]})", style="dim", ratio=2)
        table.add_column(f"Saturday ({self.week[5]})", style="dim", ratio=2)
        table.add_column(f"Sunday ({self.week[6]})", style="dim", ratio=2)

        return table

    def scroll_up(self):
        '''Update the first row of the table (starting hour used later by self.update())'''
        if self.top_hour > 24:
            self.top_hour = 0
        else:
            self.top_hour += 1

    def scroll_down(self):
        '''Update the first row of the table (starting hour used later by self.update())'''
        if self.top_hour > 24:
            self.top_hour = 0
        else:
            self.top_hour -= 1

    def create_row(self, hour, events):
        '''
        1. Gather all events from the same hour (row)
        2. Add string to columns if event meets the criteria
        '''
        same_hour_events = []
        for event in events:
            info = event.get_info()
            date = info["date"]
            if date[1] == hour:
                same_hour_events.append(event)

        self.table.add_row(f"{hour}\n",
                           f"{self.get_day(same_hour_events, 'Monday')}",
                           f"{self.get_day(same_hour_events, 'Tuesday')}",
                           f"{self.get_day(same_hour_events, 'Wednesday')}",
                           f"{self.get_day(same_hour_events, 'Thursday')}",
                           f"{self.get_day(same_hour_events, 'Friday')}",
                           f"{self.get_day(same_hour_events, 'Saturday')}",
                           f"{self.get_day(same_hour_events, 'Sunday')}")

    def get_day(self, same_hour_events, day):
        '''Returns event information if the days correspond'''
        for event in same_hour_events:
            info = event.get_info()
            date = info["date"]
            if date[0] == day:
                return f"{info['title']}\nID: {info['id']}"
        return ""



    def get_week(self, date):
        """Return the full week (Sunday first) of the week containing the given date.
        'date' may be a datetime or date instance (the same type is returned).
        """
        one_day = datetime.timedelta(days=1)
        day_idx = date.weekday()  # turn sunday into 0, monday into 1, etc.
        sunday = date - datetime.timedelta(days=day_idx)
        date = sunday
        for n in range(7):
            yield date.isoformat()
            date += one_day
