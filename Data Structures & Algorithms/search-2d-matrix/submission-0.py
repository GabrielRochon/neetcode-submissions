class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # Dû à l'ordonnancement du input, on peut trouver si un élément existe en passant d'une rangée à l'autre
        # On explore une rangée à la fois. Lorsque le chiffre est plus grand, on fait du binary search de la rangée

        # Idée alternative: dérouler la matrice 2D en une liste, et faire du binary search. Respecte complexité O(logm*n) imposée par le problème.

        # Problème: dérouler la liste rend la complexité O(m*n). On doit traverser la matrice sans avoir à créer de nouvelle liste.

        # Typical binary search problem moving forward
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            
            middle = (left + right) // 2
            print(left, middle, right)

            row = middle // len(matrix[0])      # 10 = [3,2]
            col = middle % len(matrix[0])       # Mod of row 

            if matrix[row][col] < target:
                left = middle + 1
            elif  matrix[row][col] > target:
                right = middle - 1
            else:
                return True

        return False

