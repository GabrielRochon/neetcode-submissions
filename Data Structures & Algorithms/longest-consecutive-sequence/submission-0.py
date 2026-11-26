class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # On examine les voisins en gardant en mémoire lesquels ont des voisins immédiatement après avec un dict
        # Enfin, on compte les voisins en traversant les groupes, en partant des clés qui n'ont pas de voisin
        # (on sait que c'est des fins de files)
        # Complexité temps: O(2n) ~= O(n), espace O(n) dict et set.
        
        next_element_exists = { }

        for num in nums:
            if num-1 in next_element_exists:
                next_element_exists[num-1] = True
                next_element_exists[num] = False
            if num+1 in next_element_exists:
                next_element_exists[num] = True
            if num+1 not in next_element_exists:
                next_element_exists[num] = False

        # Pour chaque nombre qui n'a pas de voisin immédiat, on teste pour voir la longueur de la suite
        largest_count = 0

        for key in next_element_exists.keys():
            local_count = 0
            if next_element_exists[key] == False:        # Une fin de suite
                while key in next_element_exists:
                    local_count += 1
                    key -= 1

            largest_count = max(largest_count, local_count)
        
        return largest_count;