# algo-prep

Entraînement algo pour entretiens, orienté DevOps/SRE/Cloud.
Objectif: bases solides et durables, prêtes à fignoler quand un entretien tombe.

Modèle de travail: **LeetCode pour résoudre, ce repo + Claude pour comprendre
et réviser.**

    LeetCode      = la salle de sport. Tu résous, le juge valide (edge cases, timing).
    repo + Claude = le coach. On explique le pattern avant, on review ta solution
                    après, on log pour la répétition espacée.

Ce repo ne contient donc PAS de solutions à faire tourner en local (le juge
LeetCode est meilleur). Il contient les notes de cours et le suivi.

## Ce qu'il y a dedans

- `CHEATSHEET.md`             Big-O + toolkit Python, ta référence rapide
- `PROGRESS.md`              suivi + répétition espacée ("Seul ?" = la vérité)
- `patterns/*/README.md`     par pattern: l'idée, les signaux, les outils, la
                             liste des problèmes LeetCode à faire
- `patterns/00_fundamentals/` Big-O: leçon + exercice d'analyse de complexité
                             (ça, LeetCode ne le fait pas)

## La boucle par pattern

1. Claude explique le pattern (l'idée, quand le reconnaître).
2. Tu résous les problèmes LeetCode listés dans le README du pattern, seul,
   sans regarder la solution.
3. Tu colles ton code ici + ta complexité annoncée (Time + Space). Claude review.
4. On note dans `PROGRESS.md`. Tu refais à J+2 et J+7.

Bloqué plus de ~15 min sur un problème ? Tu demandes un indice, pas la solution.

## La boucle DANS l'entretien (les 6 étapes, à ritualiser)

1. CLARIFIER    reformuler, edge cases, taille des inputs, contraintes
2. EXEMPLE      dérouler un cas à la main
3. BRUTE FORCE  la solution naïve, annoncée avec sa complexité
4. OPTIMISER    quelle structure de données fait tomber la complexité ?
5. CODER        proprement, à voix haute
6. TESTER       cas normal + limites + complexité finale

## Roadmap (ordre NeetCode, gratuit sur neetcode.io)

- [x] 0. Fondamentaux: Big-O + toolkit Python
- [ ] 1. Arrays & Hashing   (on est ici)
- [ ] 2. Two Pointers
- [ ] 3. Sliding Window
- [ ] 4. Stack
- [ ] 5. Binary Search
- [ ] 6. Linked List
- [ ] 7. Trees (BFS/DFS)

Stretch plus tard: Heap / top-K, Backtracking, Graphs, Intervals, DP.

## Rythme

~45 min/jour. Régularité > intensité. La répétition espacée (J+2, J+7) ancre
plus que le volume.
