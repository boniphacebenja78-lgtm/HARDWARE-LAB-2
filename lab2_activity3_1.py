import subprocess
import re


# Your NVMe drive detected by smartctl
DEVICE = "/dev/sda"


# Mock data used only if smartctl cannot access the drive
MOCK_SMART_OUTPUT = """
SMART overall-health self-assessment test result: PASSED

SMART/Health Information
Critical Warning:                   0x00
Temperature:                        39 Celsius
Available Spare:                    100%
Available Spare Threshold:          10%
Percentage Used:                    2%
Power On Hours:                     13004
Unsafe Shutdowns:                   146
Media and Data Integrity Errors:    0
Error Information Log Entries:      0
Temperature Sensor 1:               39 Celsius
Temperature Sensor 2:               54 Celsius
"""


def get_smart_data(device=DEVICE):
    """
    Runs smartctl and returns the raw NVMe SMART information.
    """

    try:
        result = subprocess.run(
            ["smartctl", "-a", "-d", "nvme", device],
            capture_output=True,
            text=True,
            check=False
        )

        # If smartctl returned useful output, use it
        if result.stdout.strip():
            return result.stdout

        print("Could not read SMART data. Using mock data.")
        return MOCK_SMART_OUTPUT

    except FileNotFoundError:
        print("smartctl was not found. Using mock data.")
        return MOCK_SMART_OUTPUT

    except Exception as e:
        print(f"Error reading SMART data: {e}")
        print("Using mock data.")
        return MOCK_SMART_OUTPUT


def get_number(pattern, smart_data):
    """
    Searches for a number in the SMART output.
    Returns None if the value is not found.
    """

    match = re.search(pattern, smart_data, re.MULTILINE)

    if match:
        value = match.group(1)
        value = value.replace(",", "")
        return int(value)

    return None


def parse_smart_data(smart_data):
    """
    Converts raw NVMe SMART text into a Python dictionary.
    """

    attributes = {}

    # Overall health
    health_match = re.search(
        r"SMART overall-health self-assessment test result:\s*(\w+)",
        smart_data
    )

    if health_match:
        attributes["SMART_Health"] = health_match.group(1)

    # Critical warning is hexadecimal, for example 0x00
    warning_match = re.search(
        r"Critical Warning:\s*(0x[0-9A-Fa-f]+)",
        smart_data
    )

    if warning_match:
        attributes["Critical_Warning"] = int(warning_match.group(1), 16)

    # Temperature
    attributes["Temperature_Celsius"] = get_number(
        r"Temperature:\s*(\d+)\s+Celsius",
        smart_data
    )

    # Available spare
    attributes["Available_Spare_Percent"] = get_number(
        r"Available Spare:\s*(\d+)%",
        smart_data
    )

    # Percentage used
    attributes["Percentage_Used"] = get_number(
        r"Percentage Used:\s*(\d+)%",
        smart_data
    )

    # Power-on hours
    attributes["Power_On_Hours"] = get_number(
        r"Power On Hours:\s*([\d,]+)",
        smart_data
    )

    # Unsafe shutdowns
    attributes["Unsafe_Shutdowns"] = get_number(
        r"Unsafe Shutdowns:\s*([\d,]+)",
        smart_data
    )

    # Media/data integrity errors
    attributes["Media_and_Data_Integrity_Errors"] = get_number(
        r"Media and Data Integrity Errors:\s*([\d,]+)",
        smart_data
    )

    # Error information log entries
    attributes["Error_Information_Log_Entries"] = get_number(
        r"Error Information Log Entries:\s*([\d,]+)",
        smart_data
    )

    # Temperature sensors
    attributes["Temperature_Sensor_1_Celsius"] = get_number(
        r"Temperature Sensor 1:\s*(\d+)\s+Celsius",
        smart_data
    )

    attributes["Temperature_Sensor_2_Celsius"] = get_number(
        r"Temperature Sensor 2:\s*(\d+)\s+Celsius",
        smart_data
    )

    return attributes


def main():

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 3.1")
    print("NVMe S.M.A.R.T. DATA")
    print("=" * 50)

    print("\nReading S.M.A.R.T. data...")

    smart_data = get_smart_data()

    attributes = parse_smart_data(smart_data)

    print("\n--- PARSED DRIVE INFORMATION ---")

    for name, value in attributes.items():

        if name == "Critical_Warning":
            print(f"{name}: 0x{value:02X}")

        else:
            print(f"{name}: {value}")

    print("\nS.M.A.R.T. data parsing complete.")


if __name__ == "__main__":
    main()