plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = "ICE"

check = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

pt_bytes = bytearray(plaintext, "utf-8")

key_index = 0

cyphertext = []


for byte in pt_bytes:
    ct = (byte ^ ord(key[key_index]))
    cyphertext.append(ct)
    key_index += 1
    if key_index == len(key):
        key_index = 0


hex = bytearray(cyphertext)

print(hex.hex())