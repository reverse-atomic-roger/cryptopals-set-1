test_string1 = "this is a test"
test_string2 = "wokka wokka!!!"



def string_to_bytes(string:str) -> bytes:
    some_bytes = []
    for char in string:
        some_bytes.append(ord(char))
    return bytearray(some_bytes)

def calculate_hamming(string1:str, string2:str) -> int:
    result = bytes(a ^ b for a, b in zip(string_to_bytes(string1), string_to_bytes(string2)))
    counter = 0
    for byte in result:
        for bit in bin(byte):
            if bit == "1":
                counter += 1
    
    return counter

def normalise_hamming(edit_dist:int, keysize:int) -> int:
    return edit_dist/keysize

# def rank_key_sizes(message:str, key_size_range) -> list:
#     normalised_distances = []
#     for size in key_size_range:
#         distance = normalise_hamming(calculate_hamming(message[:size], message[size:size*2]), size)
#         result = (distance, size)                                               
#         normalised_distances.append(result)
    
#     return sorted(normalised_distances, key = lambda message: message[0])

def rank_key_sizes(message:str, key_size_range:range, number_of_blocks:int) -> list:
    normalised_distances = []
    for size in key_size_range:
        distance = 0
        for block in range(number_of_blocks):
            distance += normalise_hamming(calculate_hamming(message[:size*(block+1)], message[size*(block+1):size*(block+2)]), size)
        distance /= number_of_blocks
        result = (distance, size)                                               
        normalised_distances.append(result)
    
    return sorted(normalised_distances, key = lambda message: message[0])
                  
def main():
    with open("6.txt") as file:
        cyphertext = file.readlines()
    cyphertext = "".join(cyphertext)
    results = (rank_key_sizes(cyphertext, range(2,45), 4))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()