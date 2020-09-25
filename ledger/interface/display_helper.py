from rich.table import Table
from rich import box
from rich.console import Console

console = Console() 

def show_results(results):
    if len(results) == 1:
        return
    table = Table(show_header=True, box=box.ASCII)
    table.add_column('Index')
    table.add_column('Title')
    table.add_column('Year')
    for i, result in enumerate(results):
        table.add_row(str(i+1), result.title, str(result.year))
    console.print(table)