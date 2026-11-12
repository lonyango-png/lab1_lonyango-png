#!/bin/bash

# 1. Use the file given as the first argument, or transit_session.log if none is given.
#    ${1:-default} means "the first argument, or this default if there isn't one".
LOG_FILE="${1:-transit_session.log}"

# 2. If the file does not exist, print an error and stop with exit code 1.
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: log file '$LOG_FILE' not found."
    echo "Run the simulation first (python3 road_simulation.py), or give a file name:"
    echo "  bash analyze_log.sh my_log_file.log"
    exit 1
fi

# 3. Count sessions, zebra stops and lane changes.
#    grep -c counts the lines that contain the text.
sessions=$(grep -c "New session started" "$LOG_FILE")
zebra_stops=$(grep -c "Zebra crossing! Stopping" "$LOG_FILE")
lane_changes=$(grep -c "Changing lane" "$LOG_FILE")

echo "===== LOG SUMMARY: $LOG_FILE ====="
echo "Sessions (runs)      : $sessions"
echo "Zebra crossing stops : $zebra_stops"
echo "Lane changes         : $lane_changes"
echo "----- Latest trip -----"

# 4. If the log has no sessions, there is no latest trip.
if [ "$sessions" -eq 0 ]; then
    echo "No sessions found in this log."
    exit 0
fi

# 5. Find the line number of the LAST session header, then keep only
#    that line and everything after it (the latest session).
start_line=$(grep -n "New session started" "$LOG_FILE" | tail -n 1 | cut -d: -f1)
latest=$(tail -n +"$start_line" "$LOG_FILE")

# 6. In the latest session, find the driver name and top speed.
#    sed removes everything up to and including the label, leaving just the value.
driver=$(echo "$latest" | grep "Driver *:" | tail -n 1 | sed 's/.*Driver *: *//')
top_speed=$(echo "$latest" | grep "Top speed *:" | tail -n 1 | sed 's/.*Top speed *: *//')

# 7. A session that was quit early has no trip report.
if [ -z "$driver" ]; then
    echo "The latest session did not finish, so it has no trip report."
else
    echo "Driver    : $driver"
    echo "Top speed : $top_speed"
fi
