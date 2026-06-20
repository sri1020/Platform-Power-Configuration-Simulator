from hardware.display import Display
from utils.logger import logger

class DisplayService:

    def __init__(self, display_present):
        self.display_present = display_present

    def start(self):

        if self.display_present:
            display = Display()
            display.initialize()

        else:
            logger.warning(
                "Display not present. "
                "Skipping initialization"
            )
            print(
                "Display Not Present. "
                "Skipping Display Initialization"
            )