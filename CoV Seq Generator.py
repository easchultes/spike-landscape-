amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

def read_sequence(filename):
    with open(filename, 'r') as f:
        # Skip the description line
        # next(f)
        print(f)
        # Read the sequence line
        sequence = f.readline().strip()
        sequence = ''.join(line.strip() for line in f)
    return sequence


def generate_mutations(sequence):
    mutations = []
    for i in range(len(sequence)):
        for aa in amino_acids:
            if aa != sequence[i]:
                mutation = sequence[:i] + aa + sequence[i+1:]
                mutations.append(mutation)
    return mutations

# The original sequence of the SARS-CoV-2 spike protein
original_sequence = read_sequence('P0DTC2.fasta')

mutations = generate_mutations(original_sequence)
print(f"Generated {len(mutations)} mutations.")

with open('mutations.fasta', 'w') as f:
    for i, mutation in enumerate(mutations):
        f.write(f'>mutation_{i+1}\n')
        f.write(mutation + '\n')

original_sequence = read_sequence('P0DTC2.fasta')
print(original_sequence)