def fixedxor(buffer1, buffer2) -> str:

    buf1 = int(buffer1,16)
    buf2 = int(buffer2,16)

    result = buf1 ^ buf2

    print(str(hex(result))[2:])
    return(str(hex(result))[2:])

fixedxor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")