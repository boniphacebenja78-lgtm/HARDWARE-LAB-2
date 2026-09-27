def phantom_load_monthly_kwh(standby_watts, hours_per_day=24):
    """
    Calculate monthly energy used by a device
    left in standby.
    """

    kwh_per_day = standby_watts * hours_per_day / 1000

    monthly_kwh = kwh_per_day * 30

    return monthly_kwh


if __name__ == "__main__":

    # Example standby power
    standby_watts = 1.5

    monthly_kwh = phantom_load_monthly_kwh(standby_watts)

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 2.5")
    print("=" * 50)

    print(f"\nStandby power: {standby_watts} W")
    print(f"Hours per day: 24")
    print(f"Monthly energy: {monthly_kwh:.2f} kWh")

    print("\nNext step:")
    print("Use your Lab 1 ECG billing function to calculate")
    print("the monthly GHC cost.")