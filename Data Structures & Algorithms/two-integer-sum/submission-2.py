class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Je pense initialement à faire quelque chose comme: if target-num in nums: return True
        # Le problème, c'est que valider l'existence d'un élément dans une liste est O(n),
        # donc l'algo serait O(n^2)

        # Alternative: stocker l'index dans un dictionnaire d'abord. O(n).
        # Ensuite, pour toutes les clés, inspecter s'il existe une autre clé qui égale target-clé
        # Regarder l'existence d'une clé est O(1), donc l'algo au complet fait O(1)

        # Complexité temps: O(n), pour les raisons ci-dessus
        # Complexité espace: O(n), car le dictionnaire a n entrées

        indexes = {}

        for index, num in enumerate(nums):
            indexes[num] = index

        for index, num1 in enumerate(nums):
            num2 = target-num1
            if num2 in indexes and index != indexes[num2]:
                return [index, indexes[num2]]