class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Ça me semble être un numéro de hashing
        # Fréquence -> dictionnaire d'occurrences
        # Ensuite, on place chaque valeurs dans une liste. index 1 = 1 occurrence, index 2 = 2 occurrences, etc. Taille totale = n
        # On passe enfin au-travers de cette liste à partir de la fin.

        # Complexité
        # Temps: 
        # Espace:

        # Ex. [1,2,2,4,4,4,4,4] -> { 1:1, 2:2, 4:5}
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        frequency_map = [ [] for _ in range(len(nums)) ]

        # Ex. [1,2,-1,-1,4].    4 is present 5 times so it is at index 5-1 = 4.
        for key, val in frequencies.items():
            frequency_map[val - 1].append(key)

        response = []

        for i in reversed(range(len(frequency_map))):
            if frequency_map[i] != -1 and len(response) < k:
                for num in frequency_map[i]:
                    response.append(num)

        return response
