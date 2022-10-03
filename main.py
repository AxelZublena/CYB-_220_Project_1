import time
from rich.align import Align

from rich import box
from rich.live import Live
from rich.table import Table
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

console = Console()

layout = Layout()
layout.split_column(
    Layout(name="Weekly Scheduler"),
    Layout(name="Options")
)
layout["Options"].size = 3 


import datetime
one_day = datetime.timedelta(days=1)

def get_week(date):
  """Return the full week (Sunday first) of the week containing the given date.
  'date' may be a datetime or date instance (the same type is returned).
  """
  day_idx = date.weekday()  # turn sunday into 0, monday into 1, etc.
  sunday = date - datetime.timedelta(days=day_idx)
  date = sunday
  for n in range(7):
    yield date
    date += one_day

week = [d.isoformat() for d in get_week(datetime.datetime.now().date())]

table = Table(show_header=True, header_style="bold blue", show_edge=False, expand=True)
table.add_column("Hours", style="dim", ratio=1)
table.add_column(f"Monday ({week[0]})", style="dim", ratio=2)
table.add_column(f"Tuesday ({week[1]})", style="dim", ratio=2)
table.add_column(f"Wednesday ({week[2]})", style="dim", ratio=2)
table.add_column(f"Thursday ({week[3]})", style="dim", ratio=2)
table.add_column(f"Friday ({week[4]})", style="dim", ratio=2)
table.add_column(f"Saturday ({week[5]})", style="dim", ratio=2)
table.add_column(f"Sunday ({week[6]})", style="dim", ratio=2)
for hour in range(25):
    table.add_row(f"{hour}")

table_panel = Panel(table, style="")
# table_panel = Panel(
#     Align.center(
#         Group("\n", Align.center(table)),
#         vertical="middle",
#     ),
#     box=box.ROUNDED,
#     padding=(1, 2),
#     title="[b red]Thanks for trying out Rich!",
#     border_style="bright_blue",
# )



cmds = Table.grid(padding=(4,4))
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_column(justify="left")
cmds.add_row("[bold green]'a'[/bold green]: Add event",
             "[bold blue]'e'[/bold blue]: Edit event",
             "[bold red]'d'[/bold red]: Delete event")
cmds_panel = Panel(cmds, border_style="bright_blue")


layout["Weekly Scheduler"].update(table_panel)
layout["Options"].update(cmds_panel)

with Live(layout, refresh_per_second=4):  # update 4 times a second to feel fluid
    while True:
        time.sleep(0.1)  # arbitrary delay
        # update the renderable internally
