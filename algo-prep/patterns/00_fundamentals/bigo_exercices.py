"""Big-O: corrigé de référence.

Analyser la complexité d'un bout de code existant, c'est ce que LeetCode ne
teste jamais, et c'est exactement ce qu'un interviewer te demande ("et la
complexité ?"). Ce fichier garde 7 cas types annotés, à relire au besoin.

Rappels: compte les boucles, un `y in liste` est O(n), un tri est O(n log n).
"Space" = mémoire allouée en plus, hors tableau d'entrée.
"""


def somme(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    return total
# Time:  O(n)   un seul parcours
# Space: O(1)   une seule variable, indépendante de n


def toutes_les_paires(nums: list[int]) -> list[tuple[int, int]]:
    paires: list[tuple[int, int]] = []
    for a in nums:
        for b in nums:
            paires.append((a, b))
    return paires
# Time:  O(n²)  boucle dans boucle
# Space: O(n²)  la liste de sortie contient n x n paires


def contient_zero(nums: list[int]) -> bool:
    for x in nums:
        if x == 0:
            return True
    return False
# Time:  O(n)   sortie anticipée possible, mais le pire cas parcourt tout
# Space: O(1)


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
# Time:  O(log n)  l'intervalle [lo, hi] est divisé par 2 à chaque tour
# Space: O(1)


def doublons_lent(nums: list[int]) -> bool:
    for i, x in enumerate(nums):
        if x in nums[i + 1:]:
            return True
    return False
# Time:  O(n²)  le slice nums[i+1:] est reparcouru par `in`, dans une boucle
# Space: O(n)   le slice recrée une liste (jusqu'à n éléments) à chaque tour


def doublons_rapide(nums: list[int]) -> bool:
    vus: set[int] = set()
    for x in nums:
        if x in vus:
            return True
        vus.add(x)
    return False
# Time:  O(n)   un parcours, lookup set en O(1)
# Space: O(n)   le set peut contenir jusqu'à n éléments


def deux_boucles_separees(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    maximum = nums[0]
    for x in nums:
        if x > maximum:
            maximum = x
    return total + maximum
# Time:  O(n)   deux boucles séquentielles: O(n) + O(n) = O(n), pas O(n²)
# Space: O(1)
