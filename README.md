# Lab 1: FSD, but on Kigali Roads

A simulation of a self-driving car travelling from ALU Rwanda to the Kigali Convention Centre.

The road is a Python list (one item = one 100 m segment). The car reacts to speed limit signs, zebra crossings and buses.

**Author:** Liam Luke Onyango (GitHub: `lonyango-png`)

## How to run

1. Open a terminal in this folder.
2. Run `python3 road_simulation.py` (use `python` if that is your command).
3. Enter a driver name, edit the road if you want, then choose **5. Start driving**.
4. Open the link shown in the terminal (for example `http://127.0.0.1:8008`).
5. Go back to the terminal and press Enter. The car starts to drive.

## What I wrote

### `road_simulation.py` (10 functions)

**Check the sign**

- `is_valid_sign`: accepts only `"bus"`, `"zebra"` or a number from 20 to 100 written as text.
- `get_sign_type`: returns `"bus"`, `"zebra"`, `"speed"` or `"road"`.

**Control the car**

- `get_speed_limit`: returns the sign's number as the new limit, or keeps the current one.
- `get_target_speed`: returns 0 while stopped at a zebra, otherwise the limit.
- `adjust_speed`: moves the speed one step towards the target (+5 or -20) without overshooting.
- `count_signs`: counts speed signs, zebras and buses.

**Input and summary**

- `ask_for_number`: keeps asking until the input is a whole number in range.
- `insert_sign`: inserts a sign at a position, with bounds checking.
- `replace_sign`: replaces the sign at an index, with bounds checking.
- `get_journey_summary`: returns the signs passed, the road length, and the start and end names.

### `analyze_log.sh`

A Bash script that summarises the log file (see below).

### Provided files

`engine.py`, `transit_program.py` and `index.html` were provided and are not edited. No external libraries are used.

## Log analyser

Each run adds its events to `transit_session.log`. To summarise it:

```bash
bash analyze_log.sh                # reads transit_session.log
bash analyze_log.sh other.log      # reads the file you give it
```

It prints:

- the number of sessions
- the number of zebra crossing stops
- the number of lane changes
- the driver name and top speed of the latest trip

If the file does not exist, it prints an error and exits with code 1.

## Notes

- The assignment says a zebra stop lasts 5 seconds, but the starter code sets `ZEBRA_WAIT = 15`. My facilitator (Herve Musangwa) said either is acceptable, so I kept 15.
- `ask_for_number` handles bad input (letters, decimals, empty lines, out-of-range numbers) with a message and an example, and asks again.