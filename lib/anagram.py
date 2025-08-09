class Anagram:
    def __init__(self, word): # Initialize the Anagram class with a word
        self.word = word.lower() # Convert the word to lowercase for case-insensitive comparison

    def match(self, word_list): # Find anagrams of the word in the provided list
        return [
            w for w in word_list
            if sorted(w.lower()) == sorted(self.word)
            and w.lower() != self.word
        ]
    
# Example usage:
 anagram = Anagram("listen")
 print(anagram.match(["enlist", "google", "inlets", "banana"]))
# Output: ['enlist', 'inlets']  
