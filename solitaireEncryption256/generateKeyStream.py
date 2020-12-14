import sys
import random

def show_help(exit=True):
    print("usage: " + sys.argv[0] + " [-f filename] [-s size]")
    if exit: exit()

def generate_keystream(size, seed=None):
    ky = list()
    for i in range(1, size+1):
        ky.append(i)

    if seed != None:
        random.seed(seed)

    random.shuffle(ky)
    return ky
    

def write_keystream_to_file(keystream, filename='ks'):
    fd = open(filename, 'w')
    stream = ""
    for e in keystream: 
        stream += (e + " ")
    fd.write(stream)
    fd.flush()
    fd.close()


if __name__ == "__main__":
    if "--help" in sys.argv:
        show_help()
    # TODO: add command line flag support for -f and -s

    generate_keystream(256)

