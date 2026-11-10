"""Coordinated bilateral joint trajectory example (simulation only).
Angles are illustrative placeholders, not calibrated humanoid joint limits.
"""
from math import cos, pi

REST = {"left_shoulder": 0.0, "right_shoulder": 0.0,
        "left_elbow": 20.0, "right_elbow": 20.0}
NAMASKAR = {"left_shoulder": 55.0, "right_shoulder": -55.0,
            "left_elbow": 55.0, "right_elbow": 55.0}

def smoothstep(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 3*t*t - 2*t*t*t

def interpolate(start: dict, goal: dict, t: float) -> dict:
    """Interpolate all joints with the same smooth progress parameter."""
    s = smoothstep(t)
    return {joint: start[joint] + (goal[joint] - start[joint]) * s
            for joint in start}

def trajectory(duration_s=1.8, samples=10):
    for i in range(samples + 1):
        t = i / samples
        yield duration_s*t, interpolate(REST, NAMASKAR, t)

if __name__ == "__main__":
    for time_s, joints in trajectory():
        print(f"{time_s:4.2f}s  {joints}")
