import sys
import random

def show_help(exit=True):
    print("usage: " + sys.argv[0] + " [-f filename] [-s size]")
    if exit: exit()

def generate_keystream(size=94, seed=None):
    ky = [i for i in range(1, size+1)]

    if seed != None:
        random.seed(seed)

    random.shuffle(ky)
    return ky
    

def write_keystream_to_file(keystream, filename='ks'):
    fd = open(filename, 'w')
    stream = ""
    for e in keystream: 
        stream += (str(e) + " ")
    fd.write(stream)
    fd.flush()
    fd.close()


# Main function
def generate_keystream_to_file(size=94, seed=None, filename='ks'):
    ks = generate_keystream(size, seed)
    write_keystream_to_file(ks, filename)


if __name__ == "__main__":
    if "--help" in sys.argv:
        show_help()

    # TODO: refine command line flag support for -f -s (seed) --seed --size
    generate_keystream_to_file(filename='test') 
