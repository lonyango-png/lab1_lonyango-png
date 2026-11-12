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
    #1. A sign must be text, if it's anything else (a number, None) reject it.
    if not isinstance(sign, str):
        return False
    
    #2. The two word signs ( bus and zebra) are always allowed
    if sign == "bus" or sign == "zebra":
        return True

    #3. Otherwise it must be a number written as text, like "80".
    #.  isdecimal is only True only when every character is a digit 0-9.
    if sign.isdecimal():
        number = int(sign) #turn the text "80" into the number 80

        # The number must be from 20 to 100, and written without extra zeros ( so "080" is rejected, but "80" is fine).
        if 20 <= number <= 100 and sign == str(number):
            return True

    #4. ANything that didnt't pass the above tests is rejected.
    return False


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road" (anything else).
def get_sign_type(sign):
    # Check the two word signs first.
    if sign == "bus":
        return "bus"
    if sign == "zebra":
        return "zebra"

    # A number written as text is a speed limit sign.
    if isinstance(sign, str) and sign.isdecimal():
        return "speed"

    # "road" or anything else is plain road.
    return "road"


# ==================== PART 2: TAKE ACTION ====================

# TODO 3: If the sign is a speed sign, return its number as an int. Else return current_limit.
def get_speed_limit(sign, current_limit):
    # A speed sign sets a new limit; any other sign keeps the current limit.
    if get_sign_type(sign) == "speed":
        return int(sign) # "80" (text) becomes 80 (number)
    return current_limit


# TODO 4: Return 0 while stop_timer is above 0, otherwise return limit.
def get_target_speed(limit, stop_timer):
    # While the zebra timer is running, aim for 0. Otherwise aim for the limit.
    if stop_timer > 0:
        return 0
    return limit


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    if speed < target:
        # Too slow: add ACCELERATION (5), but never go above target.
        speed = speed + ACCELERATION
        if speed > target:
            speed = target
    elif speed > target:
        # Too fast: subtract BRAKING (20), but never go below target.
        speed = speed - BRAKING
        if speed < target:
            speed = target
    return speed
    


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    speed_signs = 0
    zebras = 0
    buses = 0

    # Check every segment on the road, one at a time.
    for sign in road_list:
        sign_type = get_sign_type(sign)
        if sign_type == "speed":
            speed_signs = speed_signs + 1
        elif sign_type == "zebra":
            zebras = zebras + 1
        elif sign_type == "bus":
            buses = buses + 1

    # This order is what transit_program.py expects: (speed_signs, zebras, buses)
    return (speed_signs, zebras, buses)

    


# ==================== PART 3: SAFE INPUT AND JOURNEY SUMMARY ====================

# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number. Return the number as an int.
def ask_for_number(question, low, high):
    # Keep asking until we get a valid answer.
    while True:
        answer = input(question).strip() # strip() removes accidental spaces
        # try/except catches text that is not a whole number such as "abc", "2.5", or "".
        try:
            number = int(answer)
        except ValueError:
            print(f" '{answer}' is not a whole number. Example: type {low} or {high}.")
            continue # take you back to the top of the loop and ask again

        # if it's a number, it must e within a range.
        if number < low or number > high:
            print(f" {number} is out of range. Enter a whole number from {low} to {high}.")
            continue

        return number # only reached when the input is valid.


# TODO 8: Insert sign at position. Return False if position is not from 0 to len(road_list).
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    # Valid positions are 0 up to len(road_list); the end is allowed
    if position < 0 or position > len(road_list):
        return False

    road_list.insert(position, sign)
    return True


# TODO 9: Replace the sign at index with a new sign. Return False if index is not
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    # Valid indexes are 0 up to len(road_list) - 1; there is nothing to replace at the end.
    if index < 0 or index > len(road_list) - 1:
        return False
    road_list[index] = sign
    return True 


# TODO 10: Summarise the journey. Use a loop to count the signs we pass
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    signs_passed = 0
    #Every segment that is not plain "road" counts as a sign we pass.
    for sign in road_list:
        if get_sign_type(sign) != "road":
            signs_passed = signs_passed + 1

    length_m = len(road_list) * SEGMENT_M # number of segmets times 100m

    # order that print_report() expects: (signs_passed, length_m, START_NAME, END_NAME)
    return (signs_passed, length_m, START_NAME, END_NAME)


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
