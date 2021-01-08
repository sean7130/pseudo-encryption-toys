from keyStreamOps import *

def chiper(ks, string, decrypt=False, ks_size=95):
    ''' Default mode is encrpyt (decrypt=False)
    But can made into decrypt by setting decrypt=True
    '''
    if decrypt: op = lambda a, b : a-b
    else: op = lambda a, b : a+b

    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    print("input string:", string)
    print("generated nks:", nks)
    for i, e in enumerate(string):
        val = convert_to_val(e)
        print("previous char, val:", e, val)
        op_val = (op(val, nks[i])%ks_size)
        new_char = convert_to_char(op_val)
        print("after operation char, val:", new_char, op_val)
        ret += new_char
        print(ret)
    return ret

if __name__ == "__main__":
    ks = read_keystream_file('ks94')
    in_text = "hello world"
    text = (chiper(ks, in_text))
    num = list()
    for e in in_text: 
        num.append(ord(e))
        if ord(e) > 127:
            print(e)

    print('text:', text)
    ks = read_keystream_file('ks94')
    print(chiper(ks, text, True))

    # external_text = 'C2JOG!2U[QsPAbW,<d97/JE%Sc:D[1qy"Ej8#geBPn-]={9/u(vocWKFB<R{x]CTR'
    external_text = 'B1IOF 1TZQsO@aV,;c87.ID$Rc9CZ0qy!Dj7"fdBOm,]={8.u(vncVJEA;Q{x\BSR'
    ks = read_keystream_file('ks94')
    print(chiper(ks, external_text, True))
