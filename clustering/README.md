# Gotta Cluster 'Em All! — K-Means sui Pokémon

Esercitazione di **clustering con K-Means** applicato al dataset dei Pokémon (800 esemplari, 6 statistiche di combattimento). Il progetto è gestito con [Poetry](https://python-poetry.org/) e offre due modalità di utilizzo:

1. **Notebook** esplorativo (`notebooks/exploration.ipynb`), con analisi, grafici e interpretazione dei cluster.
2. **Pipeline Python** modulare (`src/clustering/`), eseguibile da riga di comando.

---

## Obiettivo

Raggruppare i Pokémon in base alle loro statistiche di base, in modo da individuare "profili" ricorrenti (ad esempio Pokémon veloci e offensivi, oppure lenti e molto resistenti), senza usare alcuna etichetta preesistente.

## Dataset

File: `data/pokemon.csv`.

| Colonna | Descrizione | Usata nel clustering |
| --- | --- | :-: |
| `#` | ID del Pokédex | No |
| `Name` | Nome del Pokémon | No |
| `Type 1`, `Type 2` | Tipi (variabili categoriche) | No |
| `Total` | Somma delle 6 statistiche | No |
| `HP` | Punti salute | Sì |
| `Attack` | Attacco fisico | Sì |
| `Defense` | Difesa fisica | Sì |
| `Sp. Atk` | Attacco speciale | Sì |
| `Sp. Def` | Difesa speciale | Sì |
| `Speed` | Velocità (chi attacca per primo) | Sì |
| `Generation` | Generazione di appartenenza | No |
| `Legendary` | Flag leggendario | No |

`Total` viene escluso perché è la somma delle altre statistiche: includerlo introdurrebbe informazione ridondante. Le variabili categoriche e identificative non sono adatte a K-Means, che lavora con distanze euclidee su variabili numeriche.

## Struttura del progetto

```
clustering/
├── data/
│   └── pokemon.csv              # dataset di input
├── notebooks/
│   ├── exploration.ipynb        # analisi esplorativa + clustering
│   └── PokedexCluster.csv       # output del notebook (dataset con colonna Clusters)
├── src/clustering/
│   ├── data.py                  # caricamento del CSV
│   ├── preprocessing.py         # selezione e standardizzazione delle feature
│   ├── clustering.py            # K-Means
│   ├── evaluation.py            # inertia e silhouette score
│   ├── visualization.py         # PCA e scatter plot dei cluster
│   └── pipeline.py              # orchestrazione dell'intero flusso
├── tests/
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Requisiti

- Python **3.12** (`>=3.12,<3.13`)
- [Poetry](https://python-poetry.org/docs/#installation) 2.x

Dipendenze principali: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `requests`, `ipykernel`.

## Utilizzo
Il notebook è organizzato nei seguenti passaggi:

1. **Caricamento e ispezione** del dataset.
2. **Analisi esplorativa**: boxplot delle statistiche (con `pd.melt` per portare i dati in formato lungo), pairplot e heatmap di correlazione.
3. **Preprocessing**: scelta delle feature e standardizzazione con `StandardScaler`.
4. **Scelta di k** con il metodo del gomito (*elbow method*) sull'inertia, per k da 1 a 14.
5. **K-Means** con `k-means++` e **5 cluster**.
6. **Interpretazione dei cluster**: boxplot per cluster, centroidi riportati nella scala originale, mediane per cluster.
7. **Visualizzazione finale**: grafico interattivo Flourish incorporato, esempi casuali di Pokémon per cluster e griglia di sprite ufficiali scaricati da [PokeAPI](https://github.com/PokeAPI/sprites).
8. **Export** del dataset con la colonna `Clusters` in `PokedexCluster.csv`.

### 2. Pipeline Python

Dalla cartella `clustering/`:

```bash
python -m clustering.pipeline
```

La pipeline esegue in sequenza:

1. caricamento di `data/pokemon.csv`;
2. selezione delle 6 statistiche (`HP`, `Attack`, `Defense`, `Sp. Atk`, `Sp. Def`, `Speed`);
3. standardizzazione con `StandardScaler`;
4. K-Means (`n_clusters=5`, `n_init=10`, `random_state=42`);
5. calcolo delle metriche di valutazione;
6. riduzione a 2 componenti con PCA;
7. stampa di inertia, silhouette e dei primi 20 Pokémon con il rispettivo cluster, e visualizzazione dello scatter plot nello spazio PCA.

Esempio di utilizzo come libreria:

```python
from clustering.pipeline import run_pipeline

output = run_pipeline(n_clusters=5)

print(output["metrics"])          # {'inertia': ..., 'silhouette': ...}
print(output["data"].head())      # dataset con colonna 'cluster'
```
