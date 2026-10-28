"""Simulate motor commands without connecting to physical hardware."""


def move(5.0):
    print(f"  Motor: move forward at {speed:.1f} m/s")

def stop():
    print("  Motor: STOP")


if __name__ == "__main__":
    move(2.0)
    stop()
