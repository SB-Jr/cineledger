from rich import box
from rich.table import Table
from rich.progress import track
from rich.console import Console 


_console = Console()
def get_console():
    return _console

def get_table():
    table = Table(show_header=True, box=box.ASCII)
    return table

def print(*args, **kargs):
    _console.print(*args, **kargs)