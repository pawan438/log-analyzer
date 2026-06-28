# Log Analyzer

A command-line tool that analyzes log files and provides insights such as
log level counts (ERROR, WARNING, INFO) and top repeating messages.

---

## What the Project Does

- Reads a log file from `logs/sample.log`
- Counts occurrences of ERROR, WARNING, and INFO entries
- Identifies the most frequently repeating log messages
- Outputs a clean summary report in the terminal

---


The `-v` flag mounts your local `logs/` folder into the container
so it can read your `sample.log` file.

---

## Sample Output
