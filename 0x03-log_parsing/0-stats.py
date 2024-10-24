#!/usr/bin/python3
""" Log parsing"""


import sys
import signal
import re


# Initialize metrics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 500: 0}
line_count = 0

# Regular expression to match the log format
log_pattern = re.compile(
        r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def print_metrics():
    """Print the computed metrics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def process_line(line):
    """Process a single line of log input."""
    global total_file_size
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C)"""
    print_metrics()
    sys.exit(0)


# Register the signalhandler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Register stdin line by line
try:
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except Exception as e:
    print(f"Error: {e}")

# After processing all input, print the final metrics
print_metrics()
