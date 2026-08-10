# Leçon 0: Big-O

Big-O répond à UNE question: quand l'input double, mon code met combien de
temps en plus ? (ou combien de mémoire en plus ?)

Ce n'est pas un chronomètre. C'est un taux de croissance. On ignore les
constantes et les petits termes, on garde le terme dominant:

    3n + 5      -> O(n)
    n² + 100n   -> O(n²)     (pour n grand, n² écrase 100n)
    2           -> O(1)

## Compter, concrètement

1. Une boucle sur n éléments               -> O(n)
2. Une boucle DANS une boucle (n x n)      -> O(n²)
3. Deux boucles l'une APRÈS l'autre        -> O(n) + O(n) = O(n), PAS O(n²)
4. Diviser le problème par 2 à chaque tour -> O(log n)
5. Trier                                   -> O(n log n)

Piège classique: `y in ma_liste` n'est pas gratuit, c'est O(n) (Python
parcourt la liste). Mets-le dans une boucle et tu as un O(n²) caché. Le même
test sur un `set` est O(1).

## Le move d'optimisation (ton "opti de A à Z")

    # Brute force: pour chaque élément, rechercher dans la liste
    for i in range(n):          # O(n)
        for j in range(n):      # x O(n)
            ...                 # => O(n²)

    # Optimisé: un hashmap pour se souvenir de ce qu'on a déjà vu
    vus = set()                 # O(n) mémoire
    for x in nums:              # O(n)
        if besoin in vus: ...   # O(1) lookup
        vus.add(x)              # => O(n) total

On a échangé de la mémoire (le set) contre de la vitesse. C'est le tradeoff
time/space, et c'est ce que Datadog & co veulent t'entendre expliquer.

## Ton exercice

Ouvre `bigo_exercices.py`. Pour chaque fonction, écris en commentaire:

- la complexité TEMPS
- la complexité ESPACE (mémoire en plus, hors input)
- pourquoi, en une ligne

Ne devine pas au feeling: compte les boucles, repère les `in liste`, les tris.
Quand tu as fait les 7, dis-moi et je corrige avec toi.
