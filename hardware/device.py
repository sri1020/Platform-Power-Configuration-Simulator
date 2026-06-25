class Device:
    def __init__(
        self,
        display_present,
        lid_present,
        psu_wattage
    ):
        self.display_present = display_present
        self.lid_present = lid_present
        self.psu_wattage = psu_wattage

    def show_info(self):
        print("\nPlatform Configuration")
        print(f"Display Present : {self.display_present}")
        print(f"Lid Present     : {self.lid_present}")
        print(f"PSU Wattage     : {self.psu_wattage}W")