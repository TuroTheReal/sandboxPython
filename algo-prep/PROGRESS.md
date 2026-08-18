# PROGRESS

Répétition espacée: refaire chaque problème à J+2 et J+7.
"Seul ?" = résolu sans indice ni solution. C'est la colonne qui dit vraiment si
c'est acquis. Claude tient ce fichier à jour, Arthur code.

| Date       | Problème                  | Pattern        | Temps | Seul ? | J+2       | J+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | non    | [x] 08-17 solo | [ ] 08-24 | `Counter==Counter`. Revu de mémoire le 08-17, un seul jet propre = ACQUIS. |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | oui    | [x] 08-17 | [ ] 08-24 | `set` + early-exit. Solo du 1er coup. Revu 08-17: structure de mémoire OK, slips syntaxe (`{}` vs `set()`, `.append` vs `.add`) corrigés. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | non    | [x] 08-17 | [ ] 08-24 | dict `{valeur: indice}` + enumerate. Revu 08-17: structure recallée de mémoire (enumerate inclus!), un seul slip `seen[comp]` vs `seen[num]` corrigé. O(n) espace. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | non    | [x] 08-18 | [ ] 08-25 | `defaultdict(list)` + `tuple(sorted(mot))`. Revu 08-18: charpente de mémoire, 3 slips (tuple, `if`-garde inutile, `list(values())`). Mécanisme defaultdict + `in` dict O(1) compris à fond après questions. À repasser pour la fluidité. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | non    | [ ] 08-16 | [ ] 08-21 | `Counter().most_common(k)`. O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | NON    | [ ] 08-16 **REFAIRE SEUL** | [ ] 08-21 | Préfixe/suffixe. Donné (mur émotionnel). |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | NON    | [ ] 08-19 **REFAIRE SEUL** | [ ] 08-24 | Structure de saut donnée (fiddly). Erreurs: parenthèses des méthodes, `elif` vs 3 `if`. |
| 2026-08-17 | #167 Two Sum II           | two_pointers   | ~     | ~oui   | [ ] 08-19 | [ ] 08-24 | Two-pointer sur trié. Sa propre structure, a appliqué le fix (mouvements inversés) lui-même après un seul indice. Time O(n), Space O(1). Premier quasi-solo depuis #217. |
