class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Hashing. Clé = lettres de l'anagramme en ordre, valeurs = anagrammes
        # Complexité:
        # Temps: O(n), pour traverser strs une première fois (ops sont O(1)), et bâtir la nouvelle liste O(n) aussi, total O(n)
        # Espace: O(n) pour la taille du résultat.

        anagrams = { }

        # For loop: O(n), check existence est O(1), sort est O(nlogn)
        for anagram in strs:
            key = ''.join(sorted(anagram))    # Crée une nouvelle string avec les caractères en ordre
            if key not in anagrams:
                anagrams[key] = [ anagram ]
            else:
                anagrams[key].append(anagram)

        anagram_groups = []

        # Bâtir le résultat, aussi O(n)
        for key, val in anagrams.items():
            anagram_groups.append(val)

        return anagram_groups