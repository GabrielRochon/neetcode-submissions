class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Deux pointeurs ne fonctionnerait pas: un anagramme est un ensemble de lettres mélangées en un autre mot.
        # On peut donc utiliser du hashing ici: construire un dictionnaire d'occurrences de chaque lettre pour s, puis décrémenter valeur de la clé pour chaque lettre de t
        # Si le dictionnaire d'occurrences est vide à la fin, alors on a un anagramme.

        # Complexité:
        # Temps:  O(n): O(n) pour traverser s et peupler le dictionnaire, avec O(1) pour chaque ajout,
        #               puis O(n) pour traverser t et modifier les valeurs / retirer les clés, tous deux O(1).
        #               O(1) * n + O(1) * n = O(n)
        # Espace: O(n) car le dictionnaire nécessite une clé et une valeur pour chaque caractère de s. O(2n) = O(n)

        # Optimisation
        if len(s) != len(t):
            return False

        # Peupler le dictionnaire et comparer
        occurrences = {}
        for char in s:
            if char not in occurrences:
                occurrences[char] = 1
            else:
                occurrences[char] += 1

        for char in t:
            if char not in occurrences:
                return False
            elif occurrences[char] == 1:
                del occurrences[char]
            else:
                occurrences[char] -= 1

        return len(occurrences) == 0        # True si vide car anagramme
        