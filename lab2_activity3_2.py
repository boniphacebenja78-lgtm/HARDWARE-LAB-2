from lab2_activity3_1 import get_smart_data, parse_smart_data


def check_health(attributes):
    """
    Checks NVMe SMART attributes against health thresholds.
    """

    warnings = []

    # Critical warning
    if attributes.get("Critical_Warning", 0) != 0:
        print("CRITICAL: NVMe drive reports a critical warning.")
        warnings.append("Critical Warning detected")

    # Media and data integrity errors
    if attributes.get("Media_and_Data_Integrity_Errors", 0) > 0:
        print("CRITICAL: Media and data integrity errors detected.")
        warnings.append("Media/Data integrity errors detected")

    # Temperature
    temperature = attributes.get("Temperature_Celsius")

    if temperature is not None and temperature > 50:
        print(
            f"WARNING: Drive temperature is {temperature}°C. "
            "Check cooling and airflow."
        )
        warnings.append("High temperature")

    # Power-on hours
    power_hours = attributes.get("Power_On_Hours")

    if power_hours is not None and power_hours > 35000:
        print(
            f"NOTICE: Drive has {power_hours} power-on hours. "
            "Consider proactive replacement."
        )
        warnings.append("High power-on hours")

    # Final health result
    if not warnings:
        print("HEALTHY: No threshold violations detected.")

    return warnings


def main():

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 3.2")
    print("AUTOMATED DRIVE HEALTH CHECK")
    print("=" * 50)

    print("\nReading S.M.A.R.T. data...")

    smart_data = get_smart_data()

    attributes = parse_smart_data(smart_data)

    print("\n--- HEALTH CHECK ---")

    warnings = check_health(attributes)

    print("\n--- RESULT ---")

    if warnings:
        print(f"{len(warnings)} issue(s) detected.")

        for warning in warnings:
            print(f"- {warning}")

    else:
        print("Drive is operating within the defined thresholds.")


if __name__ == "__main__":
    main()