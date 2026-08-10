"""Exercice Big-O.

Pour CHAQUE fonction, remplis le bloc juste en dessous:
    # Time:  O(?)
    # Space: O(?)
    # Pourquoi: ...

Compte les boucles, repère les `y in liste` (O(n)) et les tris (O(n log n)).
Quand les 7 sont faits, préviens Claude pour la correction.

"Space" = mémoire EN PLUS que tu alloues, hors tableau d'entrée.
"""


def somme(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    return total
# Time:  O(?) On
# Space: O(?)
# Pourquoi: boucle for suur liste


def toutes_les_paires(nums: list[int]) -> list[tuple[int, int]]:
    paires: list[tuple[int, int]] = []
    for a in nums:
        for b in nums:
            paires.append((a, b))
    return paires
# Time:  O(?) On2
# Space: O(?)
# Pourquoi: boucle dans boucle


def contient_zero(nums: list[int]) -> bool:
    for x in nums:
        if x == 0:
            return True
    return False
# Time:  O(?) On
# Space: O(?)
# Pourquoi: boucle


def recherche_dichotomique(nums_tries: list[int], cible: int) -> bool:
    lo, hi = 0, len(nums_tries) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums_tries[mid] == cible:
            return True
        if nums_tries[mid] < cible:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
# Time:  O(?) On
# Space: O(?)
# Pourquoi: boucle


def doublons_lent(nums: list[int]) -> bool:
    for i, x in enumerate(nums):
        if x in nums[i + 1:]:   # regarde bien ce que fait cette ligne
            return True
    return False
# Time:  O(?) On2
# Space: O(?)
# Pourquoi: boucle et boucle pour slicing


def doublons_rapide(nums: list[int]) -> bool:
    vus: set[int] = set()
    for x in nums:
        if x in vus:
            return True
        vus.add(x)
    return False
# Time:  O(?) On
# Space: O(?) On
# Pourquoi: boucle et set


def deux_boucles_separees(nums: list[int]) -> int:
    total = 0
    for x in nums:            # premiere boucle
        total += x
    maximum = nums[0]
    for x in nums:            # seconde boucle, APRES la premiere
        if x > maximum:
            maximum = x
    return total + maximum
# Time:  O(?) On
# Space: O(?)
# Pourquoi: boucle et boucle pas dans boucle
