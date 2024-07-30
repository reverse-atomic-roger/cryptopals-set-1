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
#
# Challenge 3: take the hex encoded inout and find the single char it has been XOR'd with. Use a function to rank candidates using letter frequencies
hex_3 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b373"
letter_frequencies = {
    "a":8.2,
    "b":1.5,
    "c":2.8,
    "d":4.3,
    "e":12.7,
    "f":2.2,
    "g":2.0,
    "h":6.1,
    "i":7.0,
    "j":0.15,
    "k":0.77,
    "l":4.0,
    "m":2.4,
    "n":6.7,
    "o":7.5,
    "p":1.9,
    "q":0.095,
    "r":6.0,
    "s":6.3,
    "t":9.1,
    "u":2.8,
    "v":0.98,
    "w":2.4,
    "x":0.15,
    "y":2.0,
    "z":0.074
}
# for encoding bytes to b64 for pretty printing
import base64
# for the byteorder argument thats supposed to default but doesn't
import sys
# for getting sets of printable/alphanum characters
import string

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
#
# Challenge 1:
def challenge1(hex_string:str) -> str:
    # convert from hex to bytes
    some_bytes = bytes.fromhex(hex_string)
    # then convert to base64
    b64bytes = base64.b64encode(some_bytes)
    # then finally decode the bytes to a string
    base64string = b64bytes.decode()
    return base64string

# Challenge 2:
def challenge2(hex_string1:str, hex_string2:str) -> str:
    # convert hex to int for efficient XOR
    buffer1 = int(hex_string1, 16)
    buffer2 = int(hex_string2, 16)
    # XOR ints
    xor_result = buffer1 ^ buffer2
    # strip the "0x" from the returned hex string
    return hex(xor_result)[2:]

# Challenge 3:
def get_frequency(message:str, char:str) -> float:
    # get length of message to use as denominator for frequency calculation
    message_length = len(message)
    # initialise a counter for the letter to use as the numerator for frequency calculation
    char_counter = 0
    # loop over message and increment counter whenever we see the specified character
    for letter in message:
        if letter.lower() == char.lower():
            char_counter += 1
    # calculate frequency by dividing number of specified character by total characters in message
    frequency = char_counter/message_length * 100
    return frequency

def score_message(message:str) -> float:
    # initialise a score variable. lower is better
    score  = 0
    # loop over each possible letter and score each one, adding the letter's score to the total
    for char in string.ascii_lowercase:
        # get the frequency of the letter in the message. subtract the average frequency in english. 
        # use abs() to make all results positive so that differences don't cancel out
        score += abs(get_frequency(message, char) - letter_frequencies[char])
    return score

def extend_short_key(message:str, key:str) -> str:
    # add key repetitions until the key is as long as the message
    while len(message) < len(key):
        key += key
    return key

def generate_key_list() -> list:
    # initialise an empty list for results
    key_list = []
    # loop through every printable character
    for char in string.printable:
    # ord() returns a numeric value for each char. hex() converts it to hex notation
        key_list.append(hex(ord(char)))
    return key_list

def challenge3() -> list:
    # generate a list of possible keys, ie all printable characters
    chars = generate_key_list()

    # repeat each key so that its length matches the message length
    keys = []
    #for each key repeat key for message length extend_short_key(message, key)
    for key in chars:
        keys.append(extend_short_key(hex_3, key))

    #for each key, xor with message challenge2(message, key)
    plaintexts = []
    for key in keys:
        plaintexts.append(challenge2(hex_3, key))

    #for each output, score message(message)
    scored_texts = []
    for item in plaintexts:
        if not item.isprintable():
            continue
        scored_texts.append((score_message(item), item))

    #sort messages by score list.sort()
    scored_texts.sort()

    return scored_texts

def main():
    # print("Challenge 1:")
    # print(challenge1(hex_1))
    # if challenge1(hex_1) == base64_1:
    #     print("Challenge 1 successfully completed!\n\n")
              
    # print("Challenge 2:")
    # print(challenge2(hex_2_1, hex_2_2))
    # if challenge2(hex_2_1, hex_2_2) == hex_2_3:
    #     print("Challenge 2 successfully completed!\n\n")

    for item in challenge3():
        print(item)


if __name__ == "__main__":
    main()