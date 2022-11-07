def find_upstream(dna_sequence):
    start = dna_sequence.find("ATG")
    return dna_sequence[0:start]


def find_gene(dna_sequence):
    start = dna_sequence.find('ATG')
    return dna_sequence[start:]


def second_codon(gene_sequence):
    return gene_sequence[3:6]


def third_codon(gene_sequence):
    return gene_sequence[6:9]

def complementary_nucleotide(nucleotide):
    if nucleotide == 'T':
        return 'A'
    elif nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'


def complementary_sequence(dna_sequence):
    complementary_sequence = ''
    for i in range(len(dna_sequence)):
        complementary_sequence += complementary_nucleotide(dna_sequence[i])
    return complementary_sequence


if __name__ == "__main__":
    sequence = input('Please enter a DNA genetic sequence: ')
    start = sequence.find('ATG')
    print('\n\nOriginal sequence: ' + sequence)
    print(f'\nATG codon at bp {start + 1}')
    gene = find_gene(sequence)
    print(f'    followed by {gene[3:6]} at bp {start + 4}')
    print(f'    followed by {gene[6:9]} at bp {start + 7}')
    upstream = find_upstream(sequence)
    print(f'\nUpstream sequence: {upstream}')
    print(f'Upstream length:  {len(upstream)} bp')
    print(f'\nGene sequence: {gene}')
    print(f'Gene length:  {len(gene)} bp')
    lines = '|' * len(gene)
    print(f'[+ Strand]: {gene}')
    print(f'            {lines}')
    print(f'[- Strand]: {complementary_sequence(gene)}')