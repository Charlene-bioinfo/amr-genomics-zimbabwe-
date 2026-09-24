# parse_fasta.py - From Python for Genomic Data Science Lecture 8
from Bio import SeqIO

fasta_file = "data/sample_isolates.fasta"

print("Parsing FASTA using Biopython SeqIO...")
for record in SeqIO.parse(fasta_file, "fasta"):
    print(f"\nID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Length: {len(record.seq)} bp")
    print(f"Sequence: {str(record.seq)[:60]}...")

# Bonus: Reverse complement - Lecture 8 Quiz
from Bio.Seq import Seq
my_seq = Seq("TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGC")
print(f"\nReverse complement is: {my_seq.reverse_complement()}")
