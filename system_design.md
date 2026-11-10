# System Design Notes

## Functional decomposition

### Gripper state machine

```text
OPEN -- grip command --> CLOSING / target position
CLOSING -- target reached --> HOLDING (simulated)
HOLDING -- release command --> OPENING / target position
OPENING -- target reached --> OPEN
```

A real implementation should add timeout, over-current/force limit, servo fault and emergency-stop states. The current demo represents only OPEN and CLOSED states.

### Namaskar trajectory

Let the rest configuration be `q0` and target configuration be `q1`. For normalized time `u=t/T`, use `s(u)=3u²−2u³`. The commanded joint vector is:

`q(t) = q0 + s(u)(q1 − q0)`.

This produces zero interpolation slope at the beginning and end. It does not by itself prove collision-free or dynamically feasible motion. The actual robot model and joint limits are required for that validation.

### Lip-sync timing

A viseme event contains `(start_time, duration, label, mouth_opening)`. The renderer selects the active event from elapsed time and updates the mouth shape. Audio and viseme timing are only approximately coordinated in this demo. Production timing should use a common playback clock and measured phoneme boundaries.

## Hardware interface proposal

```text
Jetson Orin Nano (high-level application)
   |-- optional OAK-D camera input
   |-- motion / speech sequencing
   |-- proposed ROS 2 interface (not implemented here)
   |
   +--> ESP32 or supported servo controller
           |-- servo driver(s) --> arm / gripper servos
           +-- status / fault feedback (to be designed)

Battery --> protected power distribution --> motor rail
                                  +-------> regulated logic rail
```

Before implementing this architecture, confirm controller compatibility and electrical ratings from the actual component datasheets. The parts list alone is insufficient to determine pinout, protocol, current draw or safe wiring.
