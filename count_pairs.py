    """
    File: <count_pairs>

    Copyright (c) 2016 Krystal Lee

    License: MIT

    <count number of pairs in a dna strand>
    """

def count_pairs(dna, pair):
	return dna.count(pair)

dna = raw_input('Enter dna : ')
pair = raw_input('Enter pair : ')

print(count_pairs(dna, pair))
