# PROGRESS

Répétition espacée: refaire chaque problème à J+2 et J+7.
"Seul ?" = résolu sans indice ni solution. C'est la colonne qui dit vraiment si
c'est acquis. Claude tient ce fichier à jour, Arthur code.

| Date       | Problème                  | Pattern        | Temps | Seul ? | J+2       | J+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | non    | [ ] 08-13 | [ ] 08-18 | `Counter==Counter`. |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | oui    | [ ] 08-15 | [ ] 08-20 | `set` + early-exit. Solo du premier coup. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | dict `{valeur: indice}`. O(n) espace. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | non    | [ ] 08-15 | [ ] 08-20 | `defaultdict(list)` + `tuple(sorted(mot))`. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | non    | [ ] 08-16 | [ ] 08-21 | `Counter().most_common(k)`. O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | NON    | [ ] 08-16 **REFAIRE SEUL** | [ ] 08-21 | Préfixe/suffixe. Donné (mur émotionnel). |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | NON    | [ ] 08-19 **REFAIRE SEUL** | [ ] 08-24 | Structure de saut donnée (fiddly). Erreurs: parenthèses des méthodes, `elif` vs 3 `if`. |
| 2026-08-17 | #167 Two Sum II           | two_pointers   | ~     | ~oui   | [ ] 08-19 | [ ] 08-24 | Two-pointer sur trié. Sa propre structure, a appliqué le fix (mouvements inversés) lui-même après un seul indice. Time O(n), Space O(1). Premier quasi-solo depuis #217. |
