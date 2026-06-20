from hardware.lid import Lid
from utils.logger import logger


class LidService:

    def __init__(self, lid_present):
        self.lid_present = lid_present

    def start(self):

        if self.lid_present:
            logger.info(
                "Lid sensor detected"
            )
            lid = Lid()
            lid.enable()

        else:
            logger.warning(
                "Lid not present. "
                "Service disabled"
            )
            print(
                "Lid Not Present. "
                "Lid Service Disabled"
            )