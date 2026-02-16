import random

# -----------------------------
# Generate Random Air Pollution Sensor Readings
# -----------------------------
def generate_readings(num=10):
    """
    Generate random sensor readings for AI testing.
    Returns a list of values between 0 and 100.
    """
    readings = [round(random.uniform(0, 100), 2) for _ in range(num)]
    return readings


# Run the function only when this file is executed directly
if __name__ == "__main__":
    readings = generate_readings()
    print("Random sensor readings:", readings)
