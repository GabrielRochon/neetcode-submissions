class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # On va utiliser un set puisque l'addition, la suppression et regarder l'existence se fait en O(1)
        # On ne s'attend pas à avoir de lettres dupliquées de toute façon.
        # Two pointers / sliding window: left et right = 0 initialement. right += 1 pour inspecter le prochain caractère.
        # Si le caractère n'est pas dans le set, right += 1. Sinon, on retire s[left] du set et left += 1, puis on ré-évalue.

        # Complexité:
        # O(n) temps, car on fait max 2n incréments de pointeurs, et la logique d'addition / suppression / existence check est O(1)
        # O(n) espace, car set peut être de longueur n en pire cas

        unique_chars_in_window = set()

        left = right = 0
        longest_length = 0

        # Edge cases:
        # len(s) == 0. Handled, right < len(s) = 0 < 0 which is false, return longest_length which equals 0

        while right < len(s):
            if s[right] not in unique_chars_in_window:
                unique_chars_in_window.add(s[right])
                longest_length = max(longest_length, len(unique_chars_in_window))
                right += 1
            else:
                # Remove s[left], re-evaluate on next iteration
                unique_chars_in_window.remove(s[left])
                left += 1

        return longest_length
