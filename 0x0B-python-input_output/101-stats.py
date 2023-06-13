#!/usr/bin/python3
"""computer metrics module
"""

import sys

def print_statistics(total_size, status_codes):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status code.
    """
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))

lines_processed = 0
total_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        lines_processed += 1
        data = line.split()
        if len(data) >= 7:
            status_code = data[-2]
            file_size = int(data[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        if lines_processed % 10 == 0:
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    print_statistics(total_size, status_codes)
