def read_keystream_file(file_name):
    """ Reads from file name, returns a list represetning keystream
    """
    ks_str = open(file_name, "r").readline().split()
    for i in range(len(ks_str)):
        ks_str[i] = int(ks_str[i])
    return ks_str

def update_jokers(ks):
    return ks.index(27), ks.index(28)

def convert_to_val(char):
    return ord(char)-65

def convert_to_char(val):
    return chr(val+65)

def encrpyt(ks, string):
    string = string.upper().replace(" ","")
    ret = ""
    nks = generate_n_keystrings(ks, len(string))
    for i, e in enumerate(string):
        val = convert_to_val(e)
        ret += convert_to_char((val+nks[i])%26)
    return ret


def generate_n_keystrings(ks, n):
    ret = list()
    for i in range(n):
        val, ks = key_stream_shuffle(ks)
        while val == 27 or val == 28:
            val, ks = key_stream_shuffle(ks)
        ret.append(val)
    return ret

def key_stream_shuffle(ks):
    """ shuffles the keystream"""

    loc_27, loc_28 = update_jokers(ks)
    # STEP 1: swapper 
    ks[loc_27] = ks[(loc_27+1)%28]
    ks[(loc_27+1)%28] = 27

    # print(ks)
    # STEP 2: 
    ks.remove(28)
    ks.insert((loc_28+2)%28, 28)

    # STEP 3
    # compare sizes between the two jokers
    loc_27, loc_28 = update_jokers(ks)
    if loc_27 < loc_28:
        smaller = loc_27
        larger = loc_28
    else: 
        smaller = loc_28
        larger = loc_27
    # first and third part are exclusive of jokers
    first_part = ks[:smaller]
    third_part = ks[larger+1:]
    # second part is inclusive of the two jokers
    second_part = ks[smaller:larger+1]
    
    ks = third_part + second_part + first_part
    # print(ks)

    # STEP 4
    val = ks.pop()
    this_slice = ks[:val]
    ks = ks[val:]
    ks += (this_slice + [val])

    print(ks)
    if ks[0] == 28: return ks[-1], ks
    return ks[ks[0]], ks


if __name__ == "__main__":
    ks = read_keystream_file('ks1')
    print(ks)
    print(key_stream_shuffle(key_stream_shuffle(ks)[1]))
    # print(generate_n_keystrings(ks, 15))

    print(encrpyt(ks, "Lake Hylia"))

