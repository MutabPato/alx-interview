#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0

    # Maska to check the first few bits of each byte
    mask1 = 0b10000000 # 128, checks if the first bit is '1'
    mask2 = 0b11000000 # 192, checks if the first two bits are '10'

    for byte in data:
        # Only keep the last 8 bits of the integer
        # (each integer represents 1 byte)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes are in the current UTF-8 character
            # based on the first byte
            if (byte & 0b10000000) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & 0b11100000) == 0b11000000:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid starting byte for UTF-8
                return False
        else:
            # Check that byte is a continuation byte (10xxxxxx)
            if (byte & mask2) != mask1:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, we have an incomplete UTF-8 character
    return num_bytes == 0
