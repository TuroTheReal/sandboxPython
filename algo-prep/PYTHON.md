# PYTHON — méthodes & idiomes courants

À garder ouvert pendant que tu codes. La fluidité vient en TAPANT ces trucs,
pas en les lisant. Cette antisèche te débloque, elle ne remplace pas les reps.

## La règle qui te fait rater le plus

Un appel de méthode a TOUJOURS des parenthèses.

    s.lower       -> la méthode elle-même (objet, toujours "vrai"), PAS le résultat
    s.lower()     -> le résultat            <- c'est ça que tu veux

Pareil pour `.values()`, `.most_common(k)`, `.isalnum()`, `.keys()`, `.items()`...
Pas de `()` = pas d'exécution.

## Chaînes (str)

    s.lower() / s.upper()      minuscule / majuscule
    s.isalnum()                True si lettre OU chiffre (bool)
    s.isdigit()                True si que des chiffres
    s.strip()                  enlève les espaces au début/fin
    s.split(",")               découpe en liste sur le séparateur
    "-".join(liste)            recolle une liste de str avec un séparateur
    s[::-1]                    la chaîne à l'envers

## Listes

    lst.append(x)              ajoute en fin
    sorted(lst)                nouvelle liste triée (O(n log n))
    lst[::-1]                  la liste à l'envers
    [x for x in lst if cond]   comprehension: filtre / transforme
    [a for a, b in paires]     déballage de tuple dans la comprehension

## Dict / set

    d.get(cle, defaut)         lit sans planter (renvoie defaut si absent)
    d.values() / .keys() / .items()   itérer
    cle in d                   test d'appartenance O(1)
    st.add(x)                  ajouter dans un set

## collections

    from collections import Counter, defaultdict
    Counter(iterable)          compte les occurrences
    c.most_common(k)           les k plus fréquents -> [(elem, compte), ...]
    defaultdict(list)          clé absente -> []
    defaultdict(set)           clé absente -> set()
    defaultdict(int)           clé absente -> 0   (pour compter)

## Conversions

    list(x)   set(x)   tuple(x)   str(x)   int(x)
    tuple(sorted(mot))         clé hashable à partir d'un tri (une "signature")
    "".join(sorted(mot))       idem, mais en chaîne

## Boucles / indices

    for i, x in enumerate(lst)         indice + valeur en même temps
    range(deb, fin_exclue, pas)        ex: range(len(l)-1, -1, -1) = parcours à l'envers
    a // b                             division ENTIÈRE (jette le reste)
    a / b                              division normale (résultat à virgule)
