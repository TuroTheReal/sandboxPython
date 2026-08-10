# Pattern 1: Arrays & Hashing

## L'idée en une phrase

Quand tu es tenté de RE-parcourir la liste à l'intérieur d'une boucle (donc
O(n²)), remplace cette recherche par un hashmap (`dict` / `set`): lookup O(1),
et l'ensemble tombe en O(n). C'est le réflexe du n°6 de l'exo Big-O.

## Les signaux qui disent "c'est ce pattern"

- "y a-t-il un doublon ?"
- "compte les occurrences de..."
- "ai-je déjà vu X ?"
- "deux éléments dont la somme vaut K"
- "groupe les anagrammes / les éléments identiques"

Dès que tu penses "il faudrait retrouver quelque chose vu plus tôt", hashmap.

## Tes outils

| Besoin                             | Outil                       | Lookup |
|------------------------------------|-----------------------------|--------|
| "ai-je déjà vu X ?"                | `set`                       | O(1)   |
| "combien de fois X ?"              | `collections.Counter`       | O(1)   |
| "accumuler par clé sans KeyError"  | `collections.defaultdict`   | O(1)   |
| "associer une valeur à une clé"    | `dict`                      | O(1)   |

## Démo (exemple jetable, pas un exo)

Compter chaque caractère d'une chaîne.

    # BRUTE FORCE: pour chaque lettre, recompter toute la chaine
    #   s.count(c) est O(n), dans une boucle => O(n²)
    #
    # OPTIMISE: un seul passage, on incremente un compteur au vol

    def compte_lettres(s: str) -> dict[str, int]:
        compteur: dict[str, int] = {}
        for c in s:                               # O(n)
            compteur[c] = compteur.get(c, 0) + 1  # get + set dict = O(1)
        return compteur
    # Time: O(n)   Space: O(k), k = nb de caracteres distincts

Le squelette est toujours le même: **un seul passage + un dict/set pour
mémoriser au vol**. Tu vas le refaire plusieurs fois.

(`collections.Counter(s)` fait ça en une ligne. Mais comprends la version
manuelle d'abord: c'est celle qu'on te demande d'écrire au tableau.)

## À toi

- `p01_contains_duplicate.py`
- `p02_two_sum.py`

Depuis la racine du repo:

    make test FILE=algo-prep/patterns/01_arrays_hashing/test_arrays_hashing.py

Code, lance les tests, et quand c'est vert tu me montres ET tu m'annonces la
complexité (Time + Space). Bloqué plus de ~15 min ? Tu me dis, indice, pas
solution.
