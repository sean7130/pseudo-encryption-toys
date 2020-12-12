from keyStreamOps import *

def chiper(ks, string, decrypt=False):
    ''' Default mode is encrpyt (decrypt=False)
    But can made into decrypt by setting decrypt=True
    '''
    if decrypt: op = lambda a, b : a-b
    else: op = lambda a, b : a+b

    string = string.upper().replace(" ","")
    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    for i, e in enumerate(string):
        val = convert_to_val(e)
        ret += convert_to_char(op(val, nks[i])%26)
    return ret

# def decrpyt(ks, string):
#     # Assuming all chars are within 65-90
#     ret = ""
#     nks = generate_n_keystrings(ks, len(string))
#     for i, e in enumerate(string):
#         val = convert_to_val(e)
#         ret += convert_to_char((val-nks[i])%26)
#     return ret
# 

if __name__ == "__main__":
    ks = read_keystream_file('ks1')
    text = (chiper(ks, "Lake Hylia"))
    print(text)
    ks = read_keystream_file('ks1')
    print(chiper(ks, text, 'd'))
