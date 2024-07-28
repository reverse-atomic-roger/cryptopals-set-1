import string

input_data =[]

with open("4.txt") as data_file:
    input_data = data_file.readlines()

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

def get_frequency(message:str, char:str) -> float:
    message_length = len(message)
    char_counter = 0
    for letter in message:
        if letter.lower() == char.lower():
            char_counter += 1
    
    frequency = char_counter/message_length * 100

    return frequency

def score_message(message:str) -> float:
    score  = 0
    for char in string.ascii_lowercase:
        score += abs(get_frequency(message, char) - letter_frequencies[char])
    
    return score

twodresults = []
for item in input_data:
    results = []
    cyphertext = bytearray.fromhex(item)

    for char in string.printable:
        plaintext = []
        joinedtext = ""
        for byte in cyphertext:
            pt = chr(byte ^ ord(char))
            plaintext.append(pt)
            joinedtext = "".join(plaintext)
        results.append(joinedtext)
    
    filtered_list = []
    for item in results:
        if not item.isprintable():
            continue

        if not filtered_list:
            filtered_list.append((score_message(item), item))

    filtered_list.sort()

#    if len(filtered_list) > 0:
    twodresults.append(filtered_list)

for item in twodresults:
    print(item)