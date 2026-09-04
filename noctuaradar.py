from textual.app import App, ComposeResult
from textual.widgets import Header, Static

class NoctuaRadar(App):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        # Un banner estilo retro para el inicio
        yield Static("""
         _   _  ____   ____ _____ _   _   _     ____      _     ____    _    ____  
        | \ | |/ __ \ / ___|_   _| | | | / \   |  _ \    / \   |  _ \  / \  |  _ \ 
        |  \| | |  | | |     | | | | | |/ _ \  | |_) |  / _ \  | | | |/ _ \ | |_) |
        | |\  | |__| | |___  | | | |_| / ___ \ |  _ <  / ___ \ | |_| / ___ \|  _ < 
        |_| \_|\____/ \____| |_|  \___/_/   \_\|_| \_\/_/   \_\|____/_/   \_\|_| \_\
        """)
        # Aquí irían tus widgets de Dogecoin...

if __name__ == "__main__":
    app = NoctuaRadar()
    app.run()