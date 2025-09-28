from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import csv
import matplotlib.pyplot as plt

def run_blast(fasta_file, top_n=20):
    """Lance un BLASTn sur une séquence FASTA et retourne les résultats."""
    record = SeqIO.read(fasta_file, 'fasta')
    print(f"[INFO] Séquence chargée est  : {record.seq}")
    
    res = NCBIWWW.qblast("blastn", "nt", str(record.seq))
    blast = NCBIXML.read(res)
    
    results = []
    for alignment in blast.alignments[:top_n]:
        for hsp in alignment.hsps[:1]:  # premier HSP
            identity_pct = round((hsp.identities / hsp.align_length) * 100, 2)
            results.append({
                "Titre": alignment.title,
                "Longueur": alignment.length,
                "Score": hsp.score,
                "E-value": hsp.expect,
                "Identités": f"{hsp.identities}/{hsp.align_length}","%Identité": identity_pct})
    return results

def save_to_csv(results, output_file="examples/blast_results.csv"):
    """Sauvegarde les résultats dans un CSV."""
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"[INFO] Résultats sauvegardés dans {output_file}")

def plot_identities(results, output_file="examples/plot.png"):
    """Crée un graphique des pourcentages d’identité."""
    titles = [r["Titre"].split()[0] for r in results]
    identities = [r["%Identité"] for r in results]
    
    plt.figure(figsize=(8,4))
    plt.barh(titles, identities)
    plt.xlabel("% Identité")
    plt.ylabel("Séquences")
    plt.title("Top hits BLASTn")
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"[INFO] Graphique sauvegardé dans {output_file}")

def save_best_hits_to_txt(results, output_file="examples/best_hits.txt"):
    """
    Trouve les hits avec le meilleur pourcentage d'identité et les sauvegarde dans un fichier texte.

    Args:
        results (list of dict): résultats BLAST
        output_file (str): chemin du fichier texte de sortie
    """
    # Trouver le pourcentage d'identité maximum
    max_identity = max(r["%Identité"] for r in results)

    # Filtrer tous les hits avec ce pourcentage
    best_hits = [r for r in results if r["%Identité"] == max_identity]


    # Sauvegarder les meilleurs hits dans un fichier texte
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Hits avec le meilleur % d'identité ({max_identity}%):\n")
        for hit in best_hits:
            f.write(f"- {hit['Titre']}\n")

    print(f"[INFO] Meilleurs hits sauvegardés dans {output_file}")
    return best_hits

if __name__=="__main__" :
    print('hello')
    fasta_file = "DNA_Seq.fasta"
    results = run_blast(fasta_file, top_n=20)
    save_to_csv(results)
    plot_identities(results)
    save_best_hits_to_txt(results)
  
