#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


def process_line(line):
    """Processes a single line of log"""
    global total_size, line_count
    parts = line.split()
    if len(parts) < 9:
        return
    try:
        ip = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[-2]
        file_size = int(parts[-1])

        if request != '"GET /projects/260 HTTP/1.1"':
            return

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
    except (ValueError, IndexError):
        return


def signal_handler(sig, frame):
    """Handles the interrupt signal (CTRL + C)"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
