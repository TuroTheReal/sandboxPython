"""Tests du pattern Arrays & Hashing.

Lance depuis la racine du repo:
    make test FILE=algo-prep/patterns/01_arrays_hashing/test_arrays_hashing.py
"""

from p01_contains_duplicate import contains_duplicate
from p02_two_sum import two_sum


class TestContainsDuplicate:
    def test_avec_doublon(self) -> None:
        assert contains_duplicate([1, 2, 3, 1])

    def test_sans_doublon(self) -> None:
        assert not contains_duplicate([1, 2, 3, 4])

    def test_liste_vide(self) -> None:
        assert not contains_duplicate([])

    def test_un_seul_element(self) -> None:
        assert not contains_duplicate([7])

    def test_valeurs_negatives(self) -> None:
        assert contains_duplicate([-1, -2, -1])


class TestTwoSum:
    def test_exemple_1(self) -> None:
        assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]

    def test_exemple_2(self) -> None:
        assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

    def test_valeurs_identiques(self) -> None:
        assert sorted(two_sum([3, 3], 6)) == [0, 1]

    def test_valeurs_negatives(self) -> None:
        assert sorted(two_sum([-3, 4, 3, 90], 0)) == [0, 2]
