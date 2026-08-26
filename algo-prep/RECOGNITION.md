# RECOGNITION — quel pattern pour quel problème

Le réflexe d'entretien: lire l'énoncé, repérer un SIGNAL, en déduire l'outil.
Cette table est ta grille de lecture. Avec les reps, elle passe dans ta tête et
tu n'auras plus besoin de la relire.

## Signaux → réflexe

| Dans l'énoncé tu vois...                                      | Réflexe / outil |
|---------------------------------------------------------------|-----------------|
| "déjà vu ?", "doublon", "tous distincts", "unique"            | **set** (`in` O(1), `.add`) |
| "combien de fois", "fréquence", "anagramme"                   | **Counter** |
| "les K plus fréquents", "top K"                               | **Counter.most_common(k)** |
| "retrouver par valeur" (son indice, sa position, un lien)     | **dict** `{valeur: info}` (façon Two Sum) |
| "grouper par une clé / signature commune"                     | **defaultdict(list)** |
| "tableau TRIÉ" + "une paire / deux nombres qui..."            | **two pointers** convergents (left/right) |
| "sous-tableau / sous-chaîne CONTIGUË" (plus long / plus court)| **sliding window** (fenêtre + left/right) |
| "le max / min / meilleur AU FIL du parcours"                  | **accumulateur** (var dehors + `max`/`min` dedans) |
| "communs / union / différence" entre deux collections        | **opérations de sets** (`&`, `\|`, `-`) |
| "par positions / à l'envers / par pas de 2"                   | **range(start, stop, step)** |

## Le réflexe d'or (90% des optimisations)

Remplacer une **recherche** par un **hashmap**:

- `x in liste` (O(n))  →  `x in set/dict` (O(1))
- "je re-parcours pour retrouver un truc"  →  je le **mémorise** dans un set/dict au passage.

Si tu bloques sur "comment optimiser", demande-toi:
> "Qu'est-ce que je re-cherche en boucle, et est-ce que je pourrais le mémoriser
> une fois pour le retrouver en O(1) ?"

## La démarche quand tu lis un problème neuf

1. Quelle est la **structure** de l'input ? (tableau trié ? chaîne ? paires ?)
2. Qu'est-ce que je **cherche** ? (un doublon ? une paire ? le plus long ? un compte ?)
3. Ces deux réponses → un signal de la table → un outil.
4. **Brute force d'abord** (annonce sa complexité), **puis optimise** avec le bon outil.
