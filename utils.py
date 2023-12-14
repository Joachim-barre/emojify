def emojify(text : str) -> str:
    output : str = ""
    for i in text:
        if(ord(i) > 255):
            output += '?'
        else:
            output += chr(0x0001f500 + ord(i) )
    return output
