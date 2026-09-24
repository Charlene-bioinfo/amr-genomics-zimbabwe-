# gc_content.py - Lecture 4 Quiz skill
from Bio import SeqIO

def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return (g + c) / len(seq) * 100

for record in SeqIO.parse("data/sample_isolates.fasta", "fasta"):
    gc = gc_content(str(record.seq).upper())
    print(f"{record.id}: {gc:.2f}% GC")
