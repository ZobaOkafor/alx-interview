#!/usr/bin/python3
"""UTF8 Validation."""


def validUTF8(data):
    # Helper function to check if a byte starts a valid UTF-8 sequence
    def is_valid_utf8_prefix(byte, num_bytes):
        # Check if the byte has the correct prefix for a multi-byte sequence
        return (byte >> (8 - num_bytes)) == (0b11111111 >> (num_bytes - 1))

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
