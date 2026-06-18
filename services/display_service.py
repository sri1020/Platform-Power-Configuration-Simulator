from platform.display import Display


class DisplayService:

    def __init__(self, display_present):
        self.display_present = display_present

    def start(self):

        if self.display_present:
            display = Display()
            display.initialize()

        else:
            print(
                "Display Not Present. "
                "Skipping Display Initialization"
            )