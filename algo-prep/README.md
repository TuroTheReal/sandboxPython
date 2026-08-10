# algo-prep

Entraînement algo pour entretiens, orienté DevOps/SRE/Cloud, en Python.
Objectif: bases solides et durables, prêtes à fignoler quand un entretien tombe.

## Modèle 2 phases

- **Phase 1 (maintenant)**: construire la base. Fondamentaux + patterns core,
  drillés jusqu'à l'automatisme. Rythme soutenable, pas de deadline.
- **Phase 2 (entretien daté)**: fignoler. Style de la boîte, mocks chronométrés.

## Comment on bosse (learn-mode)

- Claude démontre chaque pattern UNE fois sur un exemple jetable.
- Tous les vrais problèmes: c'est TOI qui codes.
- Claude vérifie, challenge, débloque avec des indices. Jamais la solution complète.
- Chaque solution DOIT annoncer sa complexité: `# Time: O(?)  Space: O(?)`.

## La boucle d'entretien (6 étapes)

1. CLARIFIER    reformuler, edge cases, taille des inputs, contraintes
2. EXEMPLE      dérouler un cas à la main
3. BRUTE FORCE  la solution naïve, annoncée avec sa complexité
4. OPTIMISER    quelle structure de données fait tomber la complexité ?
5. CODER        proprement, à voix haute
6. TESTER       cas normal + limites + complexité finale

## Rythme

~45 min/jour. Régularité > intensité.
Répétition espacée: chaque problème résolu, le refaire à J+2 et J+7.

## Roadmap Phase 1

- [x] 0. Fondamentaux: Big-O + toolkit Python  <- on est ici
- [ ] 1. Arrays & Hashing (hashmap, set, Counter)
- [ ] 2. Two Pointers
- [ ] 3. Sliding Window
- [ ] 4. Strings / parsing (saveur DevOps: logs)
- [ ] 5. Stack
- [ ] 6. Binary Search
- [ ] 7. Récursion + BFS/DFS (arbres, graphes)

Stretch (plus tard): Heap / top-K, Intervals, DP.

## Lancer les tests

    cd algo-prep
    python -m pytest                              # tout
    python -m pytest patterns/01_arrays_hashing   # un dossier

`pytest` arrivera au premier problème de code. Pour la leçon 0 (Big-O),
rien à installer.

Référence Big-O et Python: `CHEATSHEET.md`.
Suivi d'assiduité: `PROGRESS.md`.
