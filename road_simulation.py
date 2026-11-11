"""
road_simulation.py
Full Self Driving Simulation mode in Kigali: ALU Rwanda -> Convention Center

Your job: complete TODO 1 to TODO 10 below (replace each `pass`).
Do NOT edit engine.py, index.html or transit_program.py.
Run with:   python road_simulation.py or python3 road_simulation.py
"""

SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

# Each item in the road list is ONE segment of road. On the screen each segment is 100 m long
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road","road",
    "60", "road", "road", "road", "road","80", "road", 
    "road","zebra", "road", "road","road", "road",
]


# ==================== PART 1: CHECK THE SIGN ====================

# TODO 1: Return True only if sign is text AND is "bus", "zebra",
# or a number from 20 to 100 written as text (e.g. "80"). Otherwise False.
def is_valid_sign(sign):
    pass


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road" (anything else).
def get_sign_type(sign):
    pass


# ==================== PART 2: TAKE ACTION ====================

# TODO 3: If the sign is a speed sign, return its number as an int. Else return current_limit.
def get_speed_limit(sign, current_limit):
    pass


# TODO 4: Return 0 while stop_timer is above 0, otherwise return limit.
def get_target_speed(limit, stop_timer):
    pass


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    pass


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    pass


# ==================== PART 3: SAFE INPUT AND JOURNEY SUMMARY ====================

# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number. Return the number as an int.
def ask_for_number(question, low, high):
    pass


# TODO 8: Insert sign at position. Return False if position is not from 0 to len(road_list).
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    pass


# TODO 9: Replace the sign at index with a new sign. Return False if index is not
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    pass


# TODO 10: Summarise the journey. Use a loop to count the signs we pass
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    pass


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
