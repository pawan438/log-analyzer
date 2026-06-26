#!/usr/bin/env python3
# Log Analyzer - Version 2
# Count ERROR, WARNING, INFO + find top repeating messages

import os

# path to log file
LOG_FILE = "logs/sample.log"

# -------------------------------------------------------
# function to read log file and return all lines
# -------------------------------------------------------
def read_log():
    if not os.path.exists(LOG_FILE):
        print("ERROR: Log file not found")
        exit(1)

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    return lines

# -------------------------------------------------------
# function to count ERROR, WARNING, INFO in each line
# -------------------------------------------------------
def classify_logs(lines):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}  # dict to store counts

    for line in lines:
        for level in counts:               # check each keyword in every line
            if level in line:
                counts[level] += 1         # increment count if found

    return counts

# -------------------------------------------------------
# function to find top repeating messages (frequency)
# -------------------------------------------------------
def find_patterns(lines):
    patterns = {}                          # dict to store message frequency

    for line in lines:
        parts = line.strip().split(" ", 3) # split line into max 4 parts
        if len(parts) == 4:
            message = parts[3]             # 4th part is the actual message
            if message in patterns:
                patterns[message] += 1     # seen before, increment
            else:
                patterns[message] = 1      # first time seeing this message

    # sort by most frequent first
    sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
    return sorted_patterns

# -------------------------------------------------------
# main execution
# -------------------------------------------------------
lines   = read_log()
counts  = classify_logs(lines)
patterns = find_patterns(lines)

print(f"Log file     : {LOG_FILE}")
print(f"Total lines  : {len(lines)}")
print("-" * 40)

# print level counts
print("LOG LEVEL COUNTS:")
print(f"  ERROR   : {counts['ERROR']}")
print(f"  WARNING : {counts['WARNING']}")
print(f"  INFO    : {counts['INFO']}")
print("-" * 40)

# print top 5 repeating messages
print("TOP REPEATING MESSAGES:")
for message, count in patterns[:5]:       # only show top 5
    print(f"  [{count}x]  {message}")
