from rich.console import Console
from rich.align import Align
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, SpinnerColumn
from itertools import cycle
import time
import threading

ascii_art = r"""
                                      .+-:.:::+*=:.                                         
                                  :=..::::+.                                                
                                +::..:.+.                                                   
                              +:..:..+.     ....:-::-:...:.                                 
                            ::...:..+    ...::::::-::::.:::::                               
                           -..::.::*    ...::::--::::::::.::.:                              
                          -.:...::+    ...:.-..:-:::.::-:.:.:..                             
                         .=.::-.::*   ..:-:-:::.:::::::.-::..:::                            
                         :....:.-.+   .....-:..-:.:....-=::..::.                            
                         -..:::..:+    ::::-:.:-::-:-.::::-::-..                            
                         ::::: .::.=    ...:.-:::-:..:::.=:.-..                             
                          +.::::::::-    ..::-.-::::.::::::..                               
                          :......::.:+     ...::.:::.......                                 
                           -..::::-::-:+       .:....:.         :+-                         
                            :-..:..:.:.::=-                  .+:-.                          
                              +...:::::::.::.=+:        .=+-:.:=                            
                                +:..::..:.:.::::::::..:.::..:+                              
                                  .=:...:.....:...::..:..-=.                                
                                       =+-......::..:+=                                      
"""

console = Console()

# Panele hafif glow efekti için border rengini değiştirip göstermek
console.print(
    Panel(
        Align.center(ascii_art),
        border_style="bright_cyan",
        padding=(1, 4)
    )
)

messages = cycle([
    "Initializing modules…",
    "Loading core system…",
    "Configuring environment…",
    "Calibrating subsystems…",
    "Optimizing performance…",
    "Finalizing setup…"
])

current_message = "Initializing…"

def update_message():
    global current_message
    while True:
        current_message = next(messages)
        time.sleep(0.7)

# mesaj değiştiren thread
thread = threading.Thread(target=update_message, daemon=True)
thread.start()

with Progress(
    SpinnerColumn(),  # dönen animasyon
    TextColumn("[bold cyan]{task.fields[msg]}[/]"),
    BarColumn(bar_width=60),  # daha uzun progress bar
    TextColumn("{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
    console=console
) as progress:
    task = progress.add_task("boot", total=150, msg=current_message)

    for i in range(150):
        time.sleep(0.03)
        progress.update(task, advance=1, msg=current_message)