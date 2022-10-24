import datetime

from rich.align import Align
from rich.console import Group
from event import Event
from rich import box

from rich.table import Table, box
from rich.panel import Panel


class EditWindow():
    def __init__(self):
        self.menu = self.createMenu()
        self.menu_panel = Panel(
            Align.center(
                Group("\n", Align.center(self.menu)),
                vertical="middle",
            ),
            box=box.ROUNDED,
            padding=(1, 2),
            title="[b green]Add event",
            border_style="bright_green",
        )



    def get_panel(self):
        return self.menu_panel

    def createMenu(self):

        add_table = Table.grid(padding=1)
        # add_table.columns("Day")

        sponsor_message = Table.grid(padding=1)
        sponsor_message.add_column(style="green", justify="right")
        sponsor_message.add_column(no_wrap=True)
        sponsor_message.add_row(
            "Twitter",
            "[u blue link=https://twitter.com/textualize]https://twitter.com/textualize",
        )
        sponsor_message.add_row(
            "CEO",
            "[u blue link=https://twitter.com/willmcgugan]https://twitter.com/willmcgugan",
        )
        sponsor_message.add_row(
            "Textualize", "[u blue link=https://www.textualize.io]https://www.textualize.io"
        )

        return sponsor_message 

