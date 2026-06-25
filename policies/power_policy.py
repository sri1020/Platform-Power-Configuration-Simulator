from utils.logger import logger


class PowerPolicy:

    MINIMUM_BOOT_WATTAGE = 65

    def __init__(self, wattage):
        self.wattage = wattage

    def evaluate(self):

        logger.info(
            f"PSU connected: {self.wattage}W"
        )

        if self.wattage >= self.MINIMUM_BOOT_WATTAGE:

            logger.info(
                "Normal boot path selected"
            )

            print(
                f"PSU {self.wattage}W Connected"
            )

            print(
                "Normal Boot Path Selected"
            )

            return "NORMAL_BOOT"

        logger.warning(
            "Weak power path selected"
        )

        print(
            f"PSU {self.wattage}W Connected"
        )

        print(
            "Weak Power Path Selected"
        )

        return "WEAK_POWER_BOOT"