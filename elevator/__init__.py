# https://tedweishiwang.github.io/journal/object-oriented-design-elevator.html
"""
Key points are
* Elevator has three states (or directions) : idle, UP, DOWN
* Elevator should prefer UP direction when it is idle
* Whenever external request comes it should treat it as open the door at that floor
"""