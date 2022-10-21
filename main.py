import time
import sys
import keyboard
from rich.align import Align
from schedule import Schedule

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


schedule = Schedule()

# Commands Panel
cmds = Table.grid(padding=(4,4))
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_row("[bold green]'a'[/bold green]: Add event",
             "[bold blue]'e'[/bold blue]: Edit event",
             "[bold red]'d'[/bold red]: Delete event",
             "[bold cyan3]'j'[/bold cyan3]: Scroll down",
             "[bold cyan3]'k'[/bold cyan3]: Scroll up")
cmds_panel = Panel(cmds, border_style="bright_blue")

# Add the panels to layout
layout["scheduler"].update(schedule.get_panel())
layout["cmd"].update(cmds_panel)

# Update loop
with Live(layout, refresh_per_second=4):  # update 4 times a second to feel fluid
    while True:
        if keyboard.is_pressed("j"):
            schedule.scroll_up()
        elif keyboard.is_pressed("k"):
            schedule.scroll_down()
        elif keyboard.is_pressed("q"):
            break

        layout["scheduler"].update(schedule.update())

        time.sleep(0.1)  # arbitrary delay
        # update the renderable internally
