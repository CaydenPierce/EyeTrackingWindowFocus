from i3ipc import Connection, Event

class i3focus:
    def __init__(self):
        self.i3 = Connection() # Create the Connection object that can be used to send commands and subscribe
        self.updateWinState()

    def updateWinState(self):
        self.winstate = self.i3.get_tree().find_focused().workspace().find_focused().workspace().name

    # Define a funtion to switch workspaces when eye position changes
    def on_eye_change(self, ws):
        if ws == 0:
            self.i3.command('focus output left')
        else:
            self.i3.command('focus output right')
        self.updateWinState()

