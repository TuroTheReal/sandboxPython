"""Two Sum.

Étant donné une liste d'entiers `nums` et un entier `target`, renvoie les
indices des DEUX éléments dont la somme vaut `target`.

On garantit qu'il existe exactement une solution, et tu ne peux pas utiliser
deux fois le même indice. L'ordre des deux indices renvoyés n'importe pas.

Exemples:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]   (2 + 7 = 9)
    two_sum([3, 2, 4], 6)      -> [1, 2]   (2 + 4 = 6)
    two_sum([3, 3], 6)         -> [0, 1]

Indice: pour chaque nombre x, il te manque `target - x` (son "complément").
Comment savoir en O(1) si tu as DÉJÀ croisé ce complément, ET à quel indice ?
Le set répond à "vu ou pas", mais ici tu as besoin de l'INDICE en plus.
Quel outil associe une valeur (le nombre) à une info (son indice) ?

Objectif: O(n) en temps, un seul passage. Complexité à remplir en bas.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError("À toi de coder")


# Time:  O(?)
# Space: O(?)
