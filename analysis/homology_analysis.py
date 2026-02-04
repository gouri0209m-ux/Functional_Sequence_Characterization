from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO

record = SeqIO.read("../data/input_sequence.fasta", "fasta")

print("Submitting BLAST search...")
result_handle = NCBIWWW.qblast("blastp", "nr", record.seq)

with open("../results/blast_results.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()
print("BLAST done and saved.")

print("Parsing BLAST results...")
with open("../results/blast_results.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)

with open("../results/blast_summary.txt", "w") as out:
    for alignment in blast_record.alignments[:5]:
        for hsp in alignment.hsps:
            out.write(f"Hit: {alignment.title}\n")
            out.write(f"E-value: {hsp.expect}\n")
            out.write(f"Identity: {hsp.identities}/{hsp.align_length}\n")
            out.write("-"*60 + "\n")

print("BLAST summary created.")

