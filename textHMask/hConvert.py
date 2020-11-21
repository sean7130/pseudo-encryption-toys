def str_to_bin(str_input):
    return bin(int.from_bytes(str_input.encode(), 'big'))[2:]

def bin_to_str(bin_input):
    process_binary = '0b'+ bin_input
    n = int(process_binary, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def bin_to_h(bin_input):
    return_str = ""
    for byte_input in bin_input:
        if byte_input == '1':
            return_str += "Η"
        else:
            return_str += "H"

    return return_str

def h_to_bin(h_input):
    return_bin = ""
    for h in h_input:
        if h == "Η":
            return_bin += '1'
        else:
            return_bin += '0'

    return return_bin

def encode(message):
    step1 = str_to_bin(message)
    return bin_to_h(step1)

def decode(message):
    step1 = h_to_bin(message)
    return bin_to_str(step1)