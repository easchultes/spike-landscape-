from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from itertools import combinations

# TO USE THE SCRIPT YOU HAVE TO INSTALL BIOPYTHON, THIS IS DONE WITH PIP
# THE COMMAND IS: pip install biopython

def read_sequence(filename):
    with open(filename, 'r') as f:
        # Skip the description line
        # next(f)
        print(f)
        # Read the sequence line
        sequence = f.readline().strip()
        sequence = ''.join(line.strip() for line in f)
    return sequence

# Define the protein sequence
protein_sequence = read_sequence('P0DTC2.fasta')

# Define the amino acids
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

# Initialize the sequence counter
sequence_counter = 0

# Define the output file
output_file = open('2stepmutations_packages.fasta', 'w')

# Define the log file
log_file = open('mutations_packages.log', 'w')

# Generate all 2-step mutations
for i, j in combinations(range(len(protein_sequence)), 2):
    for aa1 in amino_acids.replace(protein_sequence[i], ''):
        for aa2 in amino_acids.replace(protein_sequence[j], ''):
            # Create the mutated sequence
            mutated_sequence = list(protein_sequence)
            mutated_sequence[i] = aa1
            mutated_sequence[j] = aa2
            mutated_sequence = ''.join(mutated_sequence)

            # Write the mutated sequence to the output file
            record = SeqRecord(Seq(mutated_sequence), id=f'mut_{i}_{j}_{aa1}_{aa2}')
            SeqIO.write(record, output_file, 'fasta')
            sequence_counter += 1
            # Write the mutation to the log file
            log_file.write(f'Mutation at positions {i} and {j}: {protein_sequence[i]}->{aa1}, {protein_sequence[j]}->{aa2}\n')
            if sequence_counter == 10000000:
                print(f"The script has generated {sequence_counter} sequences so far.")

# Close the files
output_file.close()
log_file.close()

print("The process is complete.")
print(f"The script has generated {sequence_counter} sequences")