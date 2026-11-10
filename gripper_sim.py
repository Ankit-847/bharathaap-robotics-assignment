"""Simple servo-position simulation for a two-finger pen gripper.
This is a software model only; it does not connect to a servo driver.
"""
from dataclasses import dataclass

@dataclass
class Gripper:
    open_angle: float = 20.0
    closed_angle: float = 65.0
    angle: float = 20.0

    def command(self, hold: bool) -> dict:
        self.angle = self.closed_angle if hold else self.open_angle
        return {"servo_angle_deg": self.angle,
                "state": "CLOSED" if hold else "OPEN",
                "pen_state": "HELD_SIMULATED" if hold else "RELEASED"}

if __name__ == "__main__":
    g = Gripper()
    print("Grip:", g.command(True))
    print("Release:", g.command(False))
