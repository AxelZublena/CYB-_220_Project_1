import datetime

from rich.table import Table
from rich.panel import Panel

class Schedule():
    def __init__(self):
        self.top_hour = 0
        self.week = [d for d in self.get_week(datetime.datetime.now().date())]
        self.table = self.createTable()
        self.table_panel = Panel(self.table, style="")

    def get_panel(self):
        return self.table_panel

    def update(self):
        self.table = self.createTable()
        self.table_panel = Panel(self.table, style="")
        return self.table_panel



    def createTable(self):
        # Main window: schedule
        table = Table(show_header=True, header_style="bold blue", show_edge=False, expand=True)
        table.add_column("Hours", style="dim", ratio=1)
        table.add_column(f"Monday ({self.week[0]})", style="dim", ratio=2)
        table.add_column(f"Tuesday ({self.week[1]})", style="dim", ratio=2)
        table.add_column(f"Wednesday ({self.week[2]})", style="dim", ratio=2)
        table.add_column(f"Thursday ({self.week[3]})", style="dim", ratio=2)
        table.add_column(f"Friday ({self.week[4]})", style="dim", ratio=2)
        table.add_column(f"Saturday ({self.week[5]})", style="dim", ratio=2)
        table.add_column(f"Sunday ({self.week[6]})", style="dim", ratio=2)

        for hour in range(self.top_hour, 56):
            table.add_row(f"{hour%24}\n")

        return table

    def scroll_up(self):
        if self.top_hour > 24:
            self.top_hour = 0
        else:
            self.top_hour += 1

    def scroll_down(self):
        if self.top_hour > 24:
            self.top_hour = 0
        else:
            self.top_hour -= 1


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
