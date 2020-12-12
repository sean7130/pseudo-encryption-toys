from keyStreamOps import *

def encrpyt(ks, string):
    string = string.upper().replace(" ","")
    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    for i, e in enumerate(string):
        val = convert_to_val(e)
        ret += convert_to_char((val+nks[i])%26)
    return ret

def decrpyt(ks, string):
    # Assuming all chars are within 65-90
    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    for i, e in enumerate(string):
        val = convert_to_val(e)
        ret += convert_to_char((val-nks[i])%26)
    return ret

if __name__ == "__main__":
    ks = read_keystream_file('ks1')
    text = (encrpyt(ks, "Lake Hylia"))
    print(text)
    ks = read_keystream_file('ks1')
    print(decrpyt(ks, text))
