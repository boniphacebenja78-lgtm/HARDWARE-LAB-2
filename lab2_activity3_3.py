import json
import os
from datetime import datetime

from lab2_activity3_1 import get_smart_data, parse_smart_data


LOG_FILE = "smart_log.json"


def log_reading(attributes, log_file=LOG_FILE):
    """
    Saves the current SMART reading to a JSON log file.
    """

    reading = {
        "timestamp": datetime.now().isoformat(),
        "attributes": attributes
    }

    # Read existing log if it exists
    if os.path.exists(log_file):

        with open(log_file, "r") as file:
            try:
                history = json.load(file)

            except json.JSONDecodeError:
                history = []

    else:
        history = []

    # Add the new reading
    history.append(reading)

    # Save everything back to the file
    with open(log_file, "w") as file:
        json.dump(history, file, indent=4)

    print(f"Reading saved to {log_file}")


def find_increasing(log_file=LOG_FILE):
    """
    Compares the first and latest readings
    and identifies metrics that increased.
    """

    if not os.path.exists(log_file):
        print("No log file found.")
        return

    with open(log_file, "r") as file:
        history = json.load(file)

    if len(history) < 2:
        print("Not enough readings to detect trends.")
        print("Run the program again later to create another reading.")
        return

    first = history[0]["attributes"]
    latest = history[-1]["attributes"]

    print("\n--- TREND ANALYSIS ---")

    found_change = False

    for key in first:

        # Skip values that are not numbers
        if not isinstance(first[key], (int, float)):
            continue

        if key not in latest:
            continue

        if not isinstance(latest[key], (int, float)):
            continue

        old_value = first[key]
        new_value = latest[key]

        if new_value > old_value:

            print(
                f"{key}: INCREASED "
                f"({old_value} -> {new_value})"
            )

            found_change = True

        elif new_value < old_value:

            print(
                f"{key}: DECREASED "
                f"({old_value} -> {new_value})"
            )

            found_change = True

        else:

            print(
                f"{key}: STABLE "
                f"({old_value})"
            )

    if not found_change:
        print("No changes detected.")


def main():

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 3.3")
    print("SMART HISTORICAL LOGGING")
    print("=" * 50)

    print("\nReading current SMART data...")

    smart_data = get_smart_data()

    attributes = parse_smart_data(smart_data)

    # Save current reading
    log_reading(attributes)

    # Analyze previous readings
    find_increasing()


if __name__ == "__main__":
    main()