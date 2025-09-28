# DNA Sequence Alignment Tool 🔬

Un outil simple en Python pour aligner une séquence ADN avec la base **NCBI BLAST** grâce à **Biopython**.

## 🚀 Fonctionnalités
- Lire une séquence au format FASTA
- Effectuer un BLASTn via NCBI
- Extraire les meilleurs hits avec leurs scores
- Sauvegarder les résultats dans un fichier CSV
- Générer un graphique des % d’identité
-retouner les meilleurs séquences compatible avec la séquence donnée . 

## 📂 Structure du projet
-> DNA_SEQ_ALIGNMENT/ :
│── dna_seq_alignment.py       # Script principal (BLAST + export + graph)
│── DNA_Seq.fasta              # Exemple de séquence ADN
│── requirements.txt           # Liste des dépendances
│── README.md                  # Documentation du projet
├── examples/                  # Résultats d’exécution
│    ├── blast_results.csv     # Résultats en CSV
│    └── plot.png              # Graphique identité
