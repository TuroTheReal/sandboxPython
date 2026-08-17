# PROGRESS

Répétition espacée: refaire chaque problème à J+2 et J+7.
"Seul ?" = résolu sans indice ni solution. C'est la colonne qui dit vraiment si
c'est acquis. Claude tient ce fichier à jour, Arthur code.

| Date       | Problème                  | Pattern        | Temps | Seul ? | J+2       | J+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | non    | [ ] 08-13 | [ ] 08-18 | `Counter==Counter`. 2 essais avant. |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | oui    | [ ] 08-15 | [ ] 08-20 | `set` + early-exit. Solo du premier coup. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | dict `{valeur: indice}`. Débloqué sur `enumerate`. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | `defaultdict(list)` + `tuple(sorted(mot))`. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | non    | [ ] 08-16 | [ ] 08-21 | `Counter().most_common(k)`. Time O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | NON    | [ ] 08-16 **REFAIRE SEUL** | [ ] 08-21 | Préfixe/suffixe. Donné en grande partie (mur émotionnel). À refaire de zéro. |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | NON    | [ ] 08-19 **REFAIRE SEUL** | [ ] 08-24 | Two-pointer convergent. Structure de saut (isalnum) donnée/corrigée car fiddly. Erreurs récurrentes: parenthèses des méthodes, `isalnum` vs `alnum`, `elif` vs 3 `if`. Bonne introspection: identifie son gap = fluidité Python, pas l'algo. |
