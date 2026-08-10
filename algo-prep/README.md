# algo-prep

Entraînement algo pour entretiens SWE (tous types de postes, pas seulement DevOps).
Objectif: bases solides et durables, prêtes à fignoler quand un entretien tombe.

Modèle de travail: **LeetCode pour résoudre, ce repo + Claude pour comprendre
et réviser.**

    LeetCode      = la salle de sport. Tu résous, le juge valide (edge cases, timing).
    repo + Claude = le coach. On explique le pattern avant, on review ta solution
                    après, on log pour la répétition espacée.

Ce repo ne contient donc PAS de solutions à faire tourner en local (le juge
LeetCode est meilleur). Il contient les notes de cours, les listes d'exercices
et le suivi.

## Ce qu'il y a dedans

- `CHEATSHEET.md`             Big-O + toolkit Python, ta référence rapide
- `PROBLEMS.md`              les pulls d'exercices LeetCode par pattern (easy/medium/hard)
- `PROGRESS.md`              suivi + répétition espacée ("Seul ?" = la vérité)
- `patterns/*/README.md`     par pattern: l'idée, les signaux, les outils (le "concept")
- `patterns/00_fundamentals/` Big-O: leçon + exercice d'analyse de complexité

## La boucle par pattern (la méthodo)

Pour chaque step de la roadmap, on tourne ce cycle:

1. **CONCEPT (Claude)**  je t'explique le pattern: l'idée, quand le reconnaître,
   une démo jetable. Comme on a fait Big-O.
2. **PRATIQUE (toi)**    tu pioches dans la pull du pattern (`PROBLEMS.md`),
   easy/medium/hard selon ta forme, tu résous sur LeetCode sans la solution.
3. **REVIEW (Claude)**   tu colles ton code + ta complexité, je fais le retour
   (justesse, complexité réelle, propreté, idiomes Python).
4. **ANCRAGE**           on note dans `PROGRESS.md`, tu refais à J+2 et J+7.

Bloqué plus de ~15 min sur un problème ? Tu demandes un indice, pas la solution.

## La boucle DANS l'entretien (les 6 étapes, à ritualiser)

1. CLARIFIER    reformuler, edge cases, taille des inputs, contraintes
2. EXEMPLE      dérouler un cas à la main
3. BRUTE FORCE  la solution naïve, annoncée avec sa complexité
4. OPTIMISER    quelle structure de données fait tomber la complexité ?
5. CODER        proprement, à voix haute
6. TESTER       cas normal + limites + complexité finale

## Roadmap (ordre NeetCode, exercices détaillés dans PROBLEMS.md)

Core (le gros des entretiens tape ici):

- [x] 0. Fondamentaux: Big-O + toolkit Python
- [ ] 1. Arrays & Hashing   (on est ici)
- [ ] 2. Two Pointers
- [ ] 3. Sliding Window
- [ ] 4. Stack
- [ ] 5. Binary Search
- [ ] 6. Linked List
- [ ] 7. Trees (BFS/DFS)

Avancé (après le core):

- [ ] 8. Tries
- [ ] 9. Heap / Priority Queue
- [ ] 10. Backtracking
- [ ] 11. Graphs
- [ ] 12. Dynamic Programming (1-D puis 2-D)
- [ ] 13. Intervals
- [ ] 14. Greedy

## Rythme

~45 min/jour. Régularité > intensité. La répétition espacée (J+2, J+7) ancre
plus que le volume.
