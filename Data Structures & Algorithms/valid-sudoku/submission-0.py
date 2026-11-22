class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # On valide les trois propriétés d'un sudoku.
        # La complexité est _théoriquement_ O(1) comme on a une entrée fixe de 81 cellules.
        # Tant en temps qu'en espace.
        # On utilise le hashing (set) pour s'assurer qu'il n'y a pas de doublons, checks for existence en O(1).
        
        # D'abord, chaque rangée contient des chiffres uniques
        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[i][j]
                if cell in seen:
                    return False
                elif cell not in seen and cell != ".":
                    seen.add(cell)


        # Ensuite, chaque colonne contient des chiffres uniques
        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[j][i]
                if cell in seen:
                    return False
                elif cell not in seen and cell != ".":
                    seen.add(cell)

        # Enfin, s'assurer que chaque sous-matrice 3x3 possède des chiffres uniques
        for i in range(9):
            # Chaque sous-matrice. On calcule l'index à lire selon i et j
            seen = set()
            for j in range(9):
                subbox_i = (j % 3) + 3 * (i % 3)
                subbox_j = (j // 3) + 3 * (i // 3)

                cell = board[subbox_i][subbox_j]
                if cell in seen:
                    return False
                elif cell not in seen and cell != ".":
                    seen.add(cell)

        # Si tout passe, le sudoku est valide
        return True
