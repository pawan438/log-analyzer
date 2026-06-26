#!/usr/bin/env python3
# Log Analyzer - Version 1
# Basic log file reading and printing

import os

# path to log file
LOG_FILE = "logs/sample.log"

# -------------------------------------------------------
# function to read log file and return all lines
# -------------------------------------------------------
def read_log():
    if not os.path.exists(LOG_FILE):       # check file exists before opening
        print("ERROR: Log file not found")
        exit(1)

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()              # read all lines into a list

    return lines

# -------------------------------------------------------
# main execution
# -------------------------------------------------------
lines = read_log()

print(f"Log file     : {LOG_FILE}")
print(f"Total lines  : {len(lines)}")
print("-" * 40)

for line in lines:                         # loop and print each line
    print(line.strip())                    # .strip() removes extra spaces/newlines
