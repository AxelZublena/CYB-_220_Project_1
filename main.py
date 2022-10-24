import time
import sys
import keyboard
from rich.align import Align
from schedule import Schedule
from edit_window import EditWindow
from events import Events 

from rich import box
from rich.live import Live
from rich.table import Table
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout


console = Console()

# Create layout
layout = Layout()
layout.split_column(
    Layout(name="scheduler"),
    Layout(name="cmd")
)
layout["cmd"].size = 3 


events = Events()
schedule = Schedule(events.get_events())
menu = EditWindow()

# Commands Panel
cmds = Table.grid(padding=(4,4))
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_row("[bold green]'a'[/bold green]: Add event",
             "[bold blue]'e'[/bold blue]: Edit event",
             "[bold red]'d'[/bold red]: Delete event",
             "[bold cyan3]'down'[/bold cyan3]: Scroll down",
             "[bold cyan3]'up'[/bold cyan3]: Scroll up")
cmds_panel = Panel(cmds, border_style="bright_blue")

# Add the panels to layout
layout["scheduler"].update(schedule.get_panel())
# layout["scheduler"].update(menu.get_panel())
layout["cmd"].update(cmds_panel)

state = "schedule"

while True:
    # Update loop
    with Live(layout, refresh_per_second=4, screen=True):  # update 4 times a second to feel fluid
        while True:
            time.sleep(0.1)  # arbitrary delay
            if keyboard.is_pressed("up"):
                schedule.scroll_up()
            elif keyboard.is_pressed("down"):
                schedule.scroll_down()
            elif keyboard.is_pressed("a"):
                state = "add"
                break
            elif keyboard.is_pressed("d"):
                state = "del"
                break
            elif keyboard.is_pressed("e"):
                state = "edit"
                break
            elif keyboard.is_pressed("q"):
                state = "quit"
                break

            state = "schedule"
            schedule.update(events.get_events())
            layout["scheduler"].update(schedule.get_panel())

    if state == "add":
        events.add_event()
        schedule.set_events(events.get_events())
        state = "schedule"

    elif state == "del":
        events.del_event()
        state = "schedule"

    elif state == "edit":
        events.edit_event()
        state = "schedule"

    elif state == "quit":
        break


