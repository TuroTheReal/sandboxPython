# CHEATSHEET

Ta référence rapide. À rouvrir pendant chaque problème.

## Big-O: comment ça grandit quand l'input grandit

On ignore les constantes, on garde le terme dominant. `3n + 5` devient `O(n)`.

| Classe      | Nom            | Exemple typique                        | n=1000 -> ops |
|-------------|----------------|----------------------------------------|---------------|
| O(1)        | constant       | accès dict/set, `list[i]`, arithmétique| 1             |
| O(log n)    | logarithmique  | binary search (diviser par 2)          | ~10           |
| O(n)        | linéaire       | parcourir une fois                     | 1 000         |
| O(n log n)  | quasi-linéaire | `sorted()`, diviser-pour-régner        | ~10 000       |
| O(n²)       | quadratique    | double boucle imbriquée                | 1 000 000     |
| O(2^n)      | exponentiel    | récursion qui explore tout             | astronomique  |

Du meilleur (haut) au pire (bas). En entretien, on part souvent d'une O(n²)
et on la fait tomber en O(n) grâce à un hashmap. C'est LE move.

## Toolkit Python: structures et complexités

| Opération                       | list         | dict / set    | deque          |
|---------------------------------|--------------|---------------|----------------|
| accès par index `x[i]`          | O(1)         | -             | O(1) aux bouts |
| recherche `y in x`              | O(n)  PIÈGE  | O(1) moyen    | O(n)           |
| ajout en fin `.append()`        | O(1) amorti  | O(1) (`add`)  | O(1)           |
| ajout/retrait en tête           | O(n)         | -             | O(1)           |
| retrait `.pop()`                | O(1) en fin  | O(1)          | O(1) aux bouts |

`y in une_liste` est O(n): c'est le piège n°1. Si tu testes l'appartenance
en boucle, convertis en `set` d'abord -> O(1).

## Les réflexes qui transforment une O(n²) en O(n)

- "Est-ce que j'ai déjà vu X ?"          -> `set` (lookup O(1))
- "Combien de fois X apparaît ?"         -> `collections.Counter`
- "Un compteur par clé sans KeyError"    -> `collections.defaultdict(int)`
- "File d'attente aux deux bouts"        -> `collections.deque`
- Tri: `sorted(x)` est O(n log n), jamais O(n). Un tri gratuit n'existe pas.

## Time vs Space

Un hashmap coûte O(n) mémoire pour gagner du temps. C'est le tradeoff
classique: on échange de l'espace contre de la vitesse. En entretien,
annonce TOUJOURS les deux: `# Time: O(n)  Space: O(n)`.
