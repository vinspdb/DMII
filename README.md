# DMII

Benvenuto! Questo repository raccoglie le **esercitazioni del corso di Data Mining II**.

Ogni esercitazione vive in una cartella dedicata, con il proprio codice, i propri dati e un `README` che spiega come eseguirla.

## Esercitazioni

| Cartella | Argomento | Contenuto |
| --- | --- | --- |
| [`clustering/`](./clustering) | Clustering con **K-Means** | Notebook esplorativo e pipeline Python modulare sul dataset dei Pokémon |

Nuove esercitazioni verranno aggiunte nel corso del semestre.

## Come iniziare

1. Clona il repository:

   ```bash
   git clone https://github.com/vinspdb/DMII.git
   cd DMII
   ```

2. Entra nella cartella dell'esercitazione che ti interessa e segui le istruzioni del suo `README`.

## Strumenti utilizzati

- **Python** per tutte le esercitazioni
- **[Poetry](https://python-poetry.org/)** per la gestione delle dipendenze e degli ambienti virtuali
- **Jupyter Notebook** per l'analisi esplorativa
- Librerie principali: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

> Ogni esercitazione ha il proprio `pyproject.toml`, quindi ambiente e dipendenze sono indipendenti tra una cartella e l'altra.

## Struttura del repository

```
DMII/
├── README.md
└── clustering/        # Esercitazione su K-Means
    ├── data/
    ├── notebooks/
    ├── src/
    ├── tests/
    └── pyproject.toml
```
