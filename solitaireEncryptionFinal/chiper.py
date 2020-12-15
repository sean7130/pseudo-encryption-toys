from keyStreamOps import *

def chiper(ks, string, decrypt=False, ks_size=256):
    ''' Default mode is encrpyt (decrypt=False)
    But can made into decrypt by setting decrypt=True
    '''
    if decrypt: op = lambda a, b : a-b
    else: op = lambda a, b : a+b

    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    # print(string)
    # print(nks)
    for i, e in enumerate(string):
        val = convert_to_val(e)
        # print("previous val:", val)
        op_val = (op(val, nks[i])%ks_size)
        # print("after operation:", op_val, chr(op_val))
        ret += convert_to_char(op_val)
        # print(ret)
    return ret

if __name__ == "__main__":
    ks = read_keystream_file('ks1')
    in_text = "The quick brown fox jumps over the lazy dog, this is pretty cool!"
    text = (chiper(ks, in_text))
    num = list()
    for e in in_text: 
        num.append(ord(e))
        if ord(e) > 127:
            print(e)
    print("num", num)

    print(text)
    ks = read_keystream_file('ks1')
    print(chiper(ks, text, True))
