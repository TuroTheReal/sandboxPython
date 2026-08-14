# PROGRESS

Répétition espacée: refaire chaque problème à J+2 et J+7.
"Seul ?" = résolu sans indice ni solution. C'est la colonne qui dit vraiment si
c'est acquis. Claude tient ce fichier à jour, Arthur code.

| Date       | Problème                  | Pattern        | Temps | Seul ? | J+2       | J+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | non    | [ ] 08-13 | [ ] 08-18 | `Counter==Counter`. 2 essais avant. Complexité O(n)/O(k) OK après rappel "drop les constantes". |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | oui    | [ ] 08-15 | [ ] 08-20 | `set` + early-exit. Résolu seul du premier coup. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | dict `{valeur: indice}`. Débloqué sur `enumerate` + `seen[num]=i`. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | `defaultdict(list)` + signature `tuple(sorted(mot))`. A creusé defaultdict à fond. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | non    | [ ] 08-16 | [ ] 08-21 | `Counter().most_common(k)` + comprehension. Bugs désormais syntaxiques, plus algorithmiques. Time O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | NON    | [ ] 08-16 **REFAIRE SEUL** | [ ] 08-21 | Préfixe/suffixe (left×right). DONNÉ en grande partie (insight + 2 boucles) car Arthur cramé + mur émotionnel; il a assemblé et corrigé les index. PAS acquis, exception assumée. À refaire de zéro sans aide le 08-16. Time O(n), Space O(n). |
