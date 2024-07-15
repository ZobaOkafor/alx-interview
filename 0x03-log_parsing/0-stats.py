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


def signal_handler(sig, frame):
    """Handles the interrupt signal (CTRL + C)"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            ip = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = parts[-2]
            file_size = parts[-1]

            if not (status_code.isdigit() and file_size.isdigit()):
                continue

            status_code = str(status_code)
            file_size = int(file_size)

            # Update the total file size
            total_size += file_size

            # Update the status code count
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
