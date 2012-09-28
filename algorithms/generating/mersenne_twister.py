"""

    mersenne_twister.py
    This module implements the Mersenne twister algorithm.

    Mersenne Twister Overview:
    ------------------------
    Pseudorandomly generates 32-bit numbers in the range 0, ..., 2^32 - 1

    Pre: nothing
    Post: returns a generated number
    Time Complexity: 1
    Psuedo Code: http://en.wikipedia.org/wiki/Mersenne_twister

    mersenne_twister.extract_number() -> randnum

"""

twister = []
index = 0

def init_generator(seed, gen):
    mask = pow(2, 32) - 1
    for i in range(624):
        if i == 0:
            gen[i] = seed & mask
        else:
            gen[i] = (1812433253 * (gen[i - 1] ^ (gen[i - 1] >> 30)) + i)
            gen[i] = gen[i] & mask

def extract_number():
    global index
    global twister
    if twister == []:
        twister = [None]*624
        init_generator(19650218, twister)
    if index == 0:
        generate_numbers(twister)
    y = twister[index]
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & 2636928640)
    y = y ^ ((y << 15) & 4022730752)
    y = y ^ (y >> 18)
    index = (index + 1) % 624
    return y

def generate_numbers(gen):
    umask = pow(2, 31)
    lmask = pow(2, 31) - 1
    for i in range(624):
        y = (gen[i] & umask) | (gen[(i + 1) % 624] & lmask)
        gen[i] = gen[(i + 397) % 624] ^ (y >> 1)
        if y % 2 != 0:
            gen[i] = gen[i] ^ 2567483615
