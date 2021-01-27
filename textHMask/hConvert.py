import sys
import argparse

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
    return bin_to_h(str_to_bin(message))

def decode(message):
    return bin_to_str(h_to_bin(message))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Encrpyt/Decrpyt ascii text into sequences of "H')
    parser.add_argument('mode', choices=["e", "encrypt", "d", "decrypt"],
                    help='the mode the program should execute in. e/encrypt \
                    for encrypting text, d/decrypt for decrypting')
    parser.add_argument('text', nargs="*", help="text to be encrypted/decrypted")

    args = parser.parse_args()

    if args.mode == 'e' or args.mode == 'encrypt':
        print(encode(" ".join(args.text)))
    else:
        print(decode(args.text[0]))

