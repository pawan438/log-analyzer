# Docker Python App — Log Analyzer

A command-line tool that analyzes log files and provides insights such as
log level counts (ERROR, WARNING, INFO) and top repeating messages.

---

## What the Project Does

- Reads a log file from `logs/sample.log`
- Counts occurrences of ERROR, WARNING, and INFO entries
- Identifies the most frequently repeating log messages
- Outputs a clean summary report in the terminal

---

## Project Structure

docker-python-app/
├── main.py            # Main log analyzer script
├── Dockerfile         # Docker build instructions
├── requirements.txt   # Dependencies (none, uses standard library)
├── logs/
│   └── sample.log     # Your log file goes here
└── README.md


---

## How to Build the Docker Image

Make sure Docker is installed, then run:

```bash
sudo docker build -t log-app .
```

This will build the image and tag it as `log-app`.

---

## How to Run the Container

```bash
sudo docker run -v $(pwd)/logs:/app/logs log-app
```

The `-v` flag mounts your local `logs/` folder into the container
so it can read your `sample.log` file.

---

## Sample Output
