# amr_analysis.py - AMR Gene Distribution Analysis
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.Seq import Seq

# Simulate AMR gene pattern analysis from FASTA headers
data = []
for record in SeqIO.parse("data/sample_isolates.fasta", "fasta"):
    # Extract info from header
    parts = record.description.split('|')
    organism = parts[1].strip() if len(parts) > 1 else "Unknown"
    country = parts[2].strip() if len(parts) > 2 else "Unknown"
    gene = parts[3].strip() if len(parts) > 3 else "Unknown"

    seq_obj = Seq(str(record.seq))
    translated = seq_obj.translate()

    data.append({
        "Isolate": record.id,
        "Organism": organism,
        "Country": country,
        "AMR_Gene": gene,
        "Length_bp": len(record.seq),
        "Protein_Fragment": str(translated)[:20]
    })

df = pd.DataFrame(data)
print(df)

# Save summary
df.to_csv("amr_summary.csv", index=False)

# Visualization - Resistance distribution
gene_counts = df['AMR_Gene'].value_counts()
plt.figure()
gene_counts.plot(kind='bar')
plt.title('AMR Gene Distribution - Southern Africa Isolates')
plt.xlabel('Resistance Gene')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('resistance_distribution.png')
print("\nSaved: amr_summary.csv and resistance_distribution.png")

# Translation example from Lecture 8
seq = Seq("TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTAC")
print(f"\nFrame 0 Translation (Lecture 8 Quiz Q5): {seq.translate()}")
