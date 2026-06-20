from hardware.lid import Lid


class LidService:

    def __init__(self, lid_present):
        self.lid_present = lid_present

    def start(self):

        if self.lid_present:
            lid = Lid()
            lid.enable()

        else:
            print(
                "Lid Not Present. "
                "Lid Service Disabled"
            )