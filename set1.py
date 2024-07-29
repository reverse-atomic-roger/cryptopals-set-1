# test variables...
#
# Challenge 1: Convert the hex string to base64, first variable is input, second variable should be output, check with ==
hex_1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_1 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
#
# Challenge 2: take 2 equal length hex encoded buffers and XOR them. First two variables are inputs, third should be output
hex_2_1 = "1c0111001f010100061a024b53535009181c"
hex_2_2 = "686974207468652062756c6c277320657965"
hex_2_3 = "746865206b696420646f6e277420706c6179"

# for encoding bytes to b64 for pretty printing
import base64
# for the byteorder argument thats supposed to default but doesn't
import sys

# conversion functions for challenge 1. All one liners but its helping to get my head round all the data types, etc.
def convert_hex_to_bytearray(hex_string:str) -> bytearray:
    return bytearray.fromhex(hex_string)

def convert_hex_to_int(hex_string:str) -> int:
    return int(hex_string, 16)

def convert_hex_to_bytes(hex_string:str) -> bytes:
    return bytes.fromhex(hex_string)

def convert_bytes_to_base64(some_bytes:bytearray) -> bytes:
    return base64.b64encode(some_bytes)

def convert_bytes_to_hex(some_bytes:bytes) -> str:
    return some_bytes.hex()

def convert_bytearray_to_string(some_bytes:bytearray) -> str:
    return some_bytes.decode()

def convert_bytes_to_int(some_bytes:bytes) -> int:
    return int.from_bytes(some_bytes,byteorder=sys.byteorder)

def convert_base64_to_string(base64_bytes:bytes) -> str:
    return base64_bytes.decode()

def convert_base64_to_bytes(base64_string:str) -> bytes:
    return base64.b64decode(base64_string)

# Ways to bitwise XOR things:
# result = bytes(a ^ b for a, b in zip(bytes1,bytes2))
# result = int1 ^ int2

def challenge1(hex_string:str) -> str:
    # convert from hex to bytes
    some_bytes = bytes.fromhex(hex_string)
    # then convert to base64
    b64bytes = base64.b64encode(some_bytes)
    # then finally decode the bytes to a string
    base64string = b64bytes.decode()
    return base64string

def challenge2(hex_string1:str, hex_string2:str) -> str:
    # convert hex to int for efficient XOR
    buffer1 = int(hex_string1, 16)
    buffer2 = int(hex_string2, 16)
    # XOR ints
    xor_result = buffer1 ^ buffer2
    # strip the "0x" from the returned hex string
    return hex(xor_result)[2:]

def main():
    print("Challenge 1:")
    print(challenge1(hex_1))
    if challenge1(hex_1) == base64_1:
        print("Challenge 1 successfully completed!\n\n")
              
    print("Challenge 2:")
    print(challenge2(hex_2_1, hex_2_2))
    if challenge2(hex_2_1, hex_2_2) == hex_2_3:
        print("Challenge 3 successfully completed!\n\n")

if __name__ == "__main__":
    main()