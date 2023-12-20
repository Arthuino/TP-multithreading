# TP1-multithreading

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit/main)

## Description

Le but de ce TP est de faire effectuer une tache sur plusieurs threads en parallèle.
On utilise pour ça un manager de la lib multiprocessing.

## Utilisation

### Partie Python

Lancer le manager:

```bash
python3 queueManager.py
```

Lancer un minion qui va effectuer la tache sur un thread:

```bash
python3 minion.py
```

Lancer un boss qui va envoier une tache à effectuer pour les minions:

```bash
python3 boss.py
```

Pour les tests unitaires:

```bash
python3 test_task.py
```

### Partie C++
