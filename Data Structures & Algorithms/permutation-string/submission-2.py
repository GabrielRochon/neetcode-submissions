from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Sliding window. On veut comparer une fenêtre de s1 avec une fenêtre de même taille de s2
        # On bâtit initialement un dictionnaire de fréquences pour s1. On fait de même pour s2.
        # Puis, à chaque glissement, on enlève l'élément out of bound et on ajoute le nouvel élément au dict de s2
        # Si les deux dicts matchent, retourne True. Sinon, à la fin, retourne false.

        # Complexité
        # Temps: O(n), car la fenêtre est fixe, donc O(n - len(s1) + 1) déplacements de fenêtre, simplifié en O(n)
        # Espace: O(n), car on aura len(s1) == n clés, et un entier comme valeur pour chaque clé. O(2n) simplifié en O(n)

        left = 0
        right = len(s1) - 1
        
        # Edge cases: 
        # 1. len(s1) > len(s2). On sait automatiquement que la permutation est impossible.
        # 2. len(s1) == 0 ou len(s2) == 0. Impossible car 1 est la longueur min.
        if len(s1) > len(s2):
            return False

        s1_frequencies = Counter(s1)
        s2_frequencies = Counter(s2[0:len(s1)])

        if s1_frequencies == s2_frequencies:
            return True

        
        while right < len(s2) - 1:      # -1 to prevent s2[right] being out of bound when moving at L37
            # Move left
            if s2_frequencies[s2[left]] > 1:
                s2_frequencies[s2[left]] -= 1
            else:
                del s2_frequencies[s2[left]]
            left += 1

            # Move right
            right += 1
            if s2[right] in s2_frequencies:
                s2_frequencies[s2[right]] += 1
            else:
                s2_frequencies[s2[right]] = 1

            # Evaluate
            if s1_frequencies == s2_frequencies:
                return True

        return False