#!/usr/bin/python3
"""UTF8 Validation."""


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        # Get the binary representation of the byte
        bin_byte = bin(byte)[2:].zfill(8)

        if num_bytes == 0:
            # Determine how many bytes are needed for the character
            if bin_byte.startswith('0'):
                num_bytes = 0  # 1-byte character
            elif bin_byte.startswith('110'):
                num_bytes = 1  # 2-byte character
            elif bin_byte.startswith('1110'):
                num_bytes = 2  # 3-byte character
            elif bin_byte.startswith('11110'):
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte
        else:
            # Validate continuation byte
            if not bin_byte.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0
