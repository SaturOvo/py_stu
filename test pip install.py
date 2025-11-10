from rich import print
print ("hello ,[bold magenta]world[/bold magenta]",
       ":vampire:",locals())

from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())



from rich.console import Console

console = Console()
console.print("Hello", "World!")
console.print("Hello", "World!", style="bold red")

from rich import print

print(f"I wonder what this looks like 1 + 1 = {1 + 1}")
print({"a": [1, 2, 3], "b" : {"c" : 1}})

from rich.console import Console

console = Console()

console.print("This is some text.")
console.print("This is some text.", style="bold")
console.print("This is some text.", style="bold underline")
console.print("This is some text.", style="bold underline red")
console.print("This is some text.", style="bold underline red on black")

my_list = ["foo", "bar"]
from rich import inspect
inspect(my_list, methods=True)

