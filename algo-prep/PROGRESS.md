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
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | non    | [x] 08-18 | [ ] 08-25 | `Counter().most_common(k)`. Revu 08-18: comprehension de mémoire, nudge sur `most_common(k)` (oublié qu'il prend k). Footgun: a réutilisé `k` (paramètre) comme variable de boucle (marche par ordre d'éval, mais mauvaise habitude). O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | NON    | [ ] 08-16 **REFAIRE SEUL** | [ ] 08-21 | Préfixe/suffixe. Donné (mur émotionnel). |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | NON    | [ ] 08-19 **REFAIRE SEUL** | [ ] 08-24 | Structure de saut donnée (fiddly). Erreurs: parenthèses des méthodes, `elif` vs 3 `if`. |
| 2026-08-17 | #167 Two Sum II           | two_pointers   | ~     | oui    | [x] 08-20 | [ ] 08-27 | Two-pointer sur trié. Time O(n), Space O(1). Revu 08-20 SOLO de mémoire, avec la structure idiomatique `while left<right` (mieux que son 1er jet) = ACQUIS. |
| 2026-08-20 | #11 Container Most Water  | two_pointers   | ~     | non    | [ ] 08-22 | [ ] 08-27 | Two-pointer: bouge le mur court, aire = largeur × min(hauteurs). Guidé sur le pattern accumulateur (`max_area` hors boucle) + 2 fixes (`h * w`, comparer hauteurs pas positions); structure assemblée par lui. Time O(n), Space O(1). |
| 2026-08-24 | #121 Best Time Buy/Sell   | sliding_window | ~     | ~oui   | [ ] 08-26 | [ ] 08-31 | Accumulateur single-pass (min_price + max_profit). A DÉRIVÉ l'opti O(n²)→O(n) lui-même via questions socratiques (parti de "double boucle"). 2 fixes: `float('inf')` (pas `Max_int`), profit `price - min` pas l'inverse. |
| 2026-08-24 | #3 Longest Substring      | sliding_window | ~     | non    | [ ] 08-26 | [ ] 08-31 | Sliding window. D'abord O(n²) (fenêtre liste), puis OPTIMISÉ en O(n) (set + pointeur left + accumulateur), guidé mais assemblé par lui. A corrigé le `longest[left]` illégal sur un set → `s[left]`. A vu l'analyse amortie (while dans for reste O(n) car left ne recule jamais). Time O(n), Space O(n). |
| 2026-08-25 | #383 Ransom Note          | arrays_hashing | ~     | non    | [ ] 08-27 | [ ] 09-01 | Counter + "assez de chaque lettre" (>= par lettre, PAS == comme #242). A reconnu le réflexe Counter seul et écarté `in`. Fixes fluidité: `.items()` (2e fois), `>` vs `!=`. Consolidation. |
| 2026-08-25 | #349 Intersection Arrays  | arrays_hashing | ~     | ~oui   | [ ] 08-27 | [ ] 09-01 | `list(set(a) & set(b))` en une ligne, quasi-solo. Closure sur `&`: bien utilisé ici (intersection = communs), là où il l'avait mal mis sur #242 (qui voulait `Counter ==`). A appris `&`/`\|`/`-` sur les sets. |
