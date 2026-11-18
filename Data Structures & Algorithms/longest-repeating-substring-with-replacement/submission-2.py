class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Regardé la vidéo qui explique le problème.
        # Complexité: 
        # Temps: O(2n) sliding window + O(26) trouver la clé la + fréquente = O(26n) ~= O(n)
        # Espace: O(26) pour le dict, ~= O(1)

        left = right = 0
        max_substring_length = 0
        frequencies = { chr(65 + i) : 0 for i in range(26) }

        # On ajoute le premier caractère
        frequencies[s[right]] = 1

        while right < len(s):

            # Regarder si valide
            highest_frequency = 0
            for i in range(26):
                char_to_inspect = chr(65 + i)
                if frequencies[char_to_inspect] > highest_frequency:
                    highest_frequency = frequencies[char_to_inspect]
            
            window_length = right - left + 1
            if window_length - highest_frequency <= k:
                # Fenêtre valide
                max_substring_length = max(max_substring_length, window_length)
                right += 1
                if right < len(s):
                    frequencies[s[right]] += 1
            else:
                # Fenêtre non-valide
                frequencies[s[left]] -= 1
                left += 1

        return max_substring_length