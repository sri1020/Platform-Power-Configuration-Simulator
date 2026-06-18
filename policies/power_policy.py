class PowerPolicy:

    MINIMUM_BOOT_WATTAGE = 65

    def __init__(self, wattage):
        self.wattage = wattage

    def evaluate(self):

        if self.wattage >= self.MINIMUM_BOOT_WATTAGE:

            print(
                f"PSU {self.wattage}W Connected"
            )
            print(
                "Normal Boot Path Selected"
            )

            return "NORMAL_BOOT"

        print(
            f"PSU {self.wattage}W Connected"
        )
        print(
            "Weak Power Path Selected"
        )

        return "WEAK_POWER_BOOT"