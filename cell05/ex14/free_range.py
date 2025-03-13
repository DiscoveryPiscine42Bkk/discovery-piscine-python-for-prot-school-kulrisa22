import random
import time
RANGE_START = 0
RANGE_END = 100
NUM_STEPS = 10
DELAY = 0.5  

def free_range_values(start=RANGE_START, end=RANGE_END, steps=NUM_STEPS):
    print(f"Generating {steps} free-range values between {start} and {end}:")
    values = [random.randint(start, end) for _ in range(steps)]
    return values

def free_run(steps=NUM_STEPS, delay=DELAY):
    print("Starting free-range process...")
    for i in range(steps):
        value = random.randint(RANGE_START, RANGE_END)
        print(f"Step {i + 1}: Value = {value}")
        time.sleep(delay)
    print("Free-range process completed!")

if __name__ == "__main__":
    values = free_range_values()
    print(f"Generated values: {values}")
    free_run()