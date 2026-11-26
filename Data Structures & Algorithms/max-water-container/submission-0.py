class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Par logique: plus la distance entre les deux extrémités est grande, plus l'aire est grande.
        # On peut maximiser l'aire avec deux pointeurs qui forment la base, et déplacer le pointeur avec la hauteur la plus petite.

        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, base * height)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area