import sys
import yaml

from platform.device import Device

from services.display_service import DisplayService
from services.lid_service import LidService
from services.led_service import LedService

from policies.power_policy import PowerPolicy


def load_config(config_file):

    with open(config_file, "r") as file:
        return yaml.safe_load(file)


def main():

    if len(sys.argv) != 2:

        print(
            "Usage: "
            "python main.py configs/laptop.yaml"
        )

        return

    config = load_config(sys.argv[1])

    platform_cfg = config["platform"]

    device = Device(
        display_present=platform_cfg["display_present"],
        lid_present=platform_cfg["lid_present"],
        psu_wattage=platform_cfg["psu_wattage"]
    )

    device.show_info()

    print("\nStarting Services...\n")

    DisplayService(
        device.display_present
    ).start()

    LidService(
        device.lid_present
    ).start()

    policy = PowerPolicy(
        device.psu_wattage
    )

    boot_mode = policy.evaluate()

    led = LedService()

    if boot_mode == "NORMAL_BOOT":
        led.runtime()
    else:
        led.shutdown()


if __name__ == "__main__":
    main()