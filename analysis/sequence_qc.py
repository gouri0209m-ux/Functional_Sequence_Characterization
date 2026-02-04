from Bio import SeqIO

record = SeqIO.read("../data/input_sequence.fasta", "fasta")
sequence = record.seq

length = len(sequence)

aa_counts = {}
for aa in sequence:
    aa_counts[aa] = aa_counts.get(aa, 0) + 1

with open("../results/qc_summary.txt", "w") as f:
    f.write(f"Sequence ID: {record.id}\n")
    f.write(f"Description: {record.description}\n")
    f.write(f"Sequence Length: {length} amino acids\n\n")
    f.write("Amino Acid Composition:\n")
    for aa, count in aa_counts.items():
        f.write(f"{aa}: {count}\n")

print("QC complete.")
