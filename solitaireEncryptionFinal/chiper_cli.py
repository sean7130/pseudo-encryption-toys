import sys
import argparse
import chiper
from generateKeyStream import generate_keystream

parser = argparse.ArgumentParser(description='Encrpyt or decrypt using a (simulated) deck of cards')
parser.add_argument('--verbose', "-v", action='store_true', help='verbose mode')
parser.add_argument('mode', choices=["e", "encrypt", "d", "decrypt"],
                    help='the mode the program should execute in. e/encrypt \
                    for encrypting text, d/decrypt for decrypting')
parser.add_argument('seed', help='the seed used to encrypt and decrypting \
                    (you can treat as password)')
parser.add_argument('--infile', nargs='?', metavar='filename', 
                    help='text file input, use this option to omit writing on \
                    the command line')
parser.add_argument('--outfile', nargs='?', type=argparse.FileType('w'), 
                    metavar='filename', default=sys.stdout, help="output file,\
                     if unspecified, the program writes to stdout instead")
parser.add_argument('text', nargs="*", help="text to be encrypted/decrypted")

args = parser.parse_args()

if args.mode == 'e' or args.mode == 'encrypt':
    do_decrypt = False
else:
    do_decrypt = True


if args.verbose: 
    if do_decrypt:
        print("program mode set to decrypt.")
    else:
        print("program mode set to encrypt.")
    print(args)
    print(args.mode)
    print(args.seed)
    print(args.text)

ks = generate_keystream(94, args.seed)

# determine to read text from commandline or from file
if (args.infile):
    in_file = open(args.infile, "r")
    text = []
    for line in in_file.readlines():
        # remove the newline in the end
        text.append(line[:-1])
else:
    text = [" ".join(args.text)]


for line in text:
    args.outfile.write(chiper.chiper(ks, line, do_decrypt)+"\n")
