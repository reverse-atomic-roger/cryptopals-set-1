test_string1 = "this is a test"
test_string2 = "wokka wokka!!!"



def string_to_bytes(string:str) -> bytes:
    some_bytes = []
    for char in string:
        some_bytes.append(ord(char))
    return bytearray(some_bytes)

def calculate_hamming(string1:str, string2:str) -> int:
    result = bytes(a ^ b for a, b in zip(string_to_bytes(test_string1), string_to_bytes(test_string2)))
    counter = 0
    for byte in result:
        for bit in bin(byte):
            if bit == "1":
                counter += 1
    
    return counter

print(calculate_hamming(test_string1,test_string2))