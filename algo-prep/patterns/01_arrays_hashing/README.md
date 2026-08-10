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

## Les problèmes LeetCode

La liste complète easy/medium/hard de ce pattern est dans `../../PROBLEMS.md`
(section "1. Arrays & Hashing"). Commence par les 3 easy (#217, #242, #1),
enchaîne sur les medium quand le réflexe est là.

Sur leetcode.com, sans regarder la solution. Colle-moi ton code + ta
complexité (Time + Space) après chacun, je review. Objectif: viser O(n).
