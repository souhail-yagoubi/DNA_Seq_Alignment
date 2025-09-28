```markdown
# DNA Sequence Alignment Project
## Project Overview
This project allows you to:

- Perform **BLASTn searches** for a DNA sequence against the NCBI nucleotide database.
- Save the **top hits** in a CSV file.
- Visualize the **percent identity** of hits with a simple bar chart.
- Identify and save the **best matching sequences**.
## Project Structure
dna_seq_alignment/
│
├─ data/                    # Input DNA sequences
│   └─ DNA_Seq.fasta
├─ examples/                # Output files and graphs
│   ├─ blast_results.csv
│   ├─ best_hits.csv
│   └─ best_hits.txt
├─ src/                     # Python scripts
│   └─ DNA_Seq_Alignment.py
├─ requirements.txt         # Python dependencies
└─ README.md
## Installation

1. Clone the project :

```bash
git clone https://github.com/souhail-yagoubi/DNA_Seq_Alignment.git
cd DNA_Seq_Alignment
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Put your DNA sequence in `data/DNA_Seq.fasta`.
2. Run the script:

```bash
python src/DNA_Seq_Alignment.py
```

3. Outputs will appear in `examples/`:

* `blast_results.csv` → top 20 hits
* `best_hits.csv` → hits with the highest identity
* `best_hits.txt` → readable list of best hits
* `plot.png` → bar chart of % identity

## Libraries Used

* Python ≥3.8
* [Biopython](https://biopython.org/)
* [Matplotlib](https://matplotlib.org/)

