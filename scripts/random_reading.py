import random

def generate_readings(num=10):
    """
    Generate random sensor readings (0-100) for testing AI models.
    """
    readings = [round(random.uniform(0, 100), 2) for _ in range(num)]
    return readings

if __name__ == "__main__":
    readings = generate_readings()
    print("Random readings:", readings)
