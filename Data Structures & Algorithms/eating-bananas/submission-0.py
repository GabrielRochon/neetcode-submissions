class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # On teste chaque k e [1, max(piles)] pour voir quel est le premier pour lequel Koko peut tout manger en-deçà de h heures.
        # On retourne la première réponse.
        # Pas optimisé: fait brute-force, de 1 à max(piles). Complexité temps est O(n*m). Pas optimal...
        # Optimisé: utilise Binary Search pour trouver le chiffre k pour lequel une vitesse devient gérable pour Koko., Devient O(log(n*m)) temps!
        
        # Complexité espace: O(1) pas de DS particulière ou d'appel au stack pour récursivité

        # Edge case: on ne peut pas subdiviser les piles
        if (h == len(piles)):
            return max(piles)

        left = 1
        right = max(piles)
        last_valid_k = None

        while left <= right:

            k = (left + right) // 2    # middle

            # Évaluer combien d'heures Koko passerait à manger ces piles à cette vitesse
            hours_eaten = 0
            for pile in piles:
                hours_eaten += math.ceil(pile/k)    # ceil() car, ex. si pile=7 et k=3, alors Koko ne mangera pas pendant 2.33h, mais plutôt pendant 3h

            if hours_eaten <= h:
                # Valide. Vérifions si k plus petit est possible
                last_valid_k = k
                right = k - 1
            elif hours_eaten > h:
                # Invalide. k doit être plus grand
                left = k + 1

        return last_valid_k
