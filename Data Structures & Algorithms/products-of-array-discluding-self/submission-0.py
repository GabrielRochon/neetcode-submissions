class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # Prefix sum si je me rappelle bien.
        # On fait un produit de tous les éléments à gauche, puis de ceux à droite, et enfin on les multiplie
        # Ceci empêche d'avoir à utiliser l'opérateur de division

        # Complexité:   O(n) temps pour bâtir les produits, O(n) pour construire la réponse. Total O(n)
        #               O(n) espace pour toutes les listes de n espace

        product_from_left = []
        product_from_right = []

        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            product_from_left.append(product)

        product = 1
        for i in reversed(range(len(nums))):
            product *= nums[i]  
            product_from_right.append(product)
        
        product_from_right.reverse()

        # Compute product without current element by checking product of all elements right and all elements left
        product_without_self = []
        for i in range(len(nums)):
            if i == 0:
                product_without_self.append(product_from_right[i+1])
            elif i == len(nums) - 1:
                product_without_self.append(product_from_left[i-1])
            else:
                product_without_self.append(product_from_left[i-1] * product_from_right[i+1])

        return product_without_self