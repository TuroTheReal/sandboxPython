# PROGRESS

Répétition espacée: refaire chaque problème à J+2 et J+7.
"Seul ?" = résolu sans indice ni solution. C'est la colonne qui dit vraiment si
c'est acquis. Claude tient ce fichier à jour, Arthur code.

| Date       | Problème                | Pattern        | Temps | Seul ? | J+2       | J+7       | Notes |
|------------|-------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram      | arrays_hashing | ~     | non    | [ ] 08-13 | [ ] 08-18 | `Counter==Counter`. 2 essais avant (set&, boucle inutile). Complexité O(n)/O(k) OK après rappel "drop les constantes". |
| 2026-08-13 | #217 Contains Duplicate | arrays_hashing | ~     | oui    | [ ] 08-15 | [ ] 08-20 | `set` + early-exit. Résolu seul du premier coup. A questionné l'idiomatisme (bon réflexe). |
| 2026-08-13 | #1 Two Sum              | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | dict `{valeur: indice}`, un passage. Débloqué sur `enumerate` + l'écriture `seen[num]=i`. Ordre check-puis-stocke correct. |
| 2026-08-13 | #49 Group Anagrams      | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | `defaultdict(list)` + signature `tuple(sorted(mot))`. Débloqué en plusieurs passes (factory `list`, clé=signature pas `s[0]`, tuple pour hashabilité, `list(d.values())`). Time O(n·k log k). A creusé le concept defaultdict à fond. |
