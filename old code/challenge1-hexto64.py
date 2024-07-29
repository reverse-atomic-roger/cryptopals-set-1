import base64

hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

hexstringbytes = bytearray.fromhex(hexstring)

base64string = base64.b64encode(hexstringbytes)

target = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
result = base64string.decode()
#result = hexstringbytes.decode()

if target == result:
    print("Success!!!")

print(result)