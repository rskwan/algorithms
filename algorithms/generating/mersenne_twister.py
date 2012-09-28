"""
    mersenne_twister.py
    This module implements the Mersenne twister algorithm.

    Mersenne Twister Overview:
    ------------------------
    Pseudorandomly generates 32-bit numbers in the range 0, ..., 2^32 - 1

    Pre: nothing
    Post: returns a generated number
    Time Complexity: 1
    Psuedocode: http://en.wikipedia.org/wiki/Mersenne_twister

    m = MersenneTwister()
    m.extract_number() => randnum    

"""

class MersenneTwister:
    def __init__(self):
        self.index = 0
        self.twister = []

    def init_generator(self, seed, gen):
        mask = pow(2, 32) - 1
        for i in range(624):
            if i == 0:
                gen[i] = seed & mask
            else:
                gen[i] = (1812433253 * (gen[i - 1] ^ (gen[i - 1] >> 30)) + i)
                gen[i] &= mask

    def extract_number(self):
        if self.twister == []:
            self.twister = [None]*624
            self.init_generator(19650218, self.twister)
        if self.index == 0:
            self.generate_numbers(self.twister)
        y = self.twister[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 2636928640
        y ^= (y << 15) & 4022730752
        y ^= y >> 18
        self.index = (self.index + 1) % 624
        return y

    def generate_numbers(self, gen):
        umask = pow(2, 31)
        lmask = pow(2, 31) - 1
        for i in range(624):
            y = (gen[i] & umask) | (gen[(i + 1) % 624] & lmask)
            gen[i] = gen[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                gen[i] ^= 2567483615
