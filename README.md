# AMR Gene Distribution Analysis - Southern African Isolates
**Author:** Charlene Tanyardzwa Shiri | Medical Laboratory Scientist | Harare, Zimbabwe
**Purpose:** DAAD STEM 2027 Application Project - Demonstrating Python for Genomic Data Science skills

### Background
As a Medical Laboratory Scientist at Procare Clinical Laboratory, Harare, I report antibiotic resistance phenotypically (we test if bacteria grow with antibiotics) but lack tools to identify resistance genes. This project uses Python, Biopython, and pandas to analyze public AMR data.

### Data Source
NCBI Pathogen Detection - Klebsiella pneumoniae and E. coli isolates from Southern Africa (Zimbabwe, South Africa, Zambia)
Link: https://www.ncbi.nlm.nih.gov/pathogens/
Sample FASTA included in `/data` folder for demonstration - includes sequences from Python for Genomic Data Science course.

### What this repo does
1. Parses FASTA files using Biopython SeqIO - Lecture 8 skills
2. Calculates GC-content - Lecture 4 skills
3. Translates DNA to protein - Lecture 8 Quiz Q5 (WASYLSYIPCSYGGAMFYVNPRSKDIIPKSY)
4. Analyzes resistance distribution using pandas & matplotlib

### Skills Demonstrated
Python, Biopython (SeqIO, Seq, reverse_complement, translate), pandas, file parsing, GC-content

### How to Run
pip install -r requirements.txt
python parse_fasta.py
python gc_content.py
python amr_analysis.py

### Key Results
- Successfully parsed 4 Southern African isolates
- GC-content analysis: 38-52% range
- Translation confirmed: WASYLSYIPCSYGGAMFYVNPRSKDIIPKSY (Frame 0)
- Visualized AMR gene distribution: blaNDM-1, blaKPC-2, blaCTX-M-15, mcr-1

### Future Work for MSc
This will be extended at Saarland University (1st choice), Jena (2nd), and Bielefeld (3rd) to build low-cost, open-source AMR surveillance pipelines for Zimbabwean labs, contributing to SDG 3.

### Course Reference
Python for Genomic Data Science - Johns Hopkins University (Coursera) - In Progress, expected Oct 2026
