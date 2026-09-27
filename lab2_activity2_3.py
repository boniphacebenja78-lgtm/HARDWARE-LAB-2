def power_at_utilization(p_idle, p_max, u):
    """
    Calculate CPU power at a given utilization.

    P(u) = P_idle + (P_max - P_idle) * u
    """
    return p_idle + (p_max - p_idle) * u


def simulate(readings, p_idle, p_max, interval_hours):
    """
    Compare always-max power with utilization-based power.
    """

    # CPU always operating at maximum power
    always_max_kwh = sum(
        p_max * interval_hours for _ in readings
    ) / 1000

    # CPU power changes according to utilization
    ondemand_kwh = sum(
        power_at_utilization(p_idle, p_max, u) * interval_hours
        for u in readings
    ) / 1000

    return always_max_kwh, ondemand_kwh


if __name__ == "__main__":

    # Example readings from Activity 2.1
    # Replace these with your actual readings if desired.
    readings = [
        0.10,
        0.15,
        0.40,
        0.55,
        0.20,
        0.10,
        0.05,
        0.30
    ]

    # Replace these with the values you used in Lab 1
    p_idle = 20
    p_max = 95

    # Activity 2.1 records once every second
    interval_hours = 1 / 3600

    always_max, ondemand = simulate(
        readings,
        p_idle,
        p_max,
        interval_hours
    )

    saved_pct = (1 - ondemand / always_max) * 100

    print("=" * 50)
    print("HSF LAB 2 - ACTIVITY 2.3")
    print("=" * 50)

    print(f"\nCPU idle power: {p_idle} W")
    print(f"CPU maximum power: {p_max} W")
    print(f"Number of readings: {len(readings)}")

    print(f"\nAlways-max energy: {always_max:.6f} kWh")
    print(f"Ondemand-style energy: {ondemand:.6f} kWh")
    print(f"Energy saved: {saved_pct:.2f}%")