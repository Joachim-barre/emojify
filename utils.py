def emojify(text : str) -> str:
    output : str = ""
    for i in text:
        if(ord(i) > 255):
            output += '?'
        else:
            output += chr(0x0001f500 + ord(i) )
    return output

def demojify(text : str) -> str:
    output : str = ""
    for i in text:
        if(i == '?' or hex(ord(i))[:-2] != "0x1f5"):
            output += '?'
        else:
            output += chr(ord(i) - 0x0001f500)
    return output
