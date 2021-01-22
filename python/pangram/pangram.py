def is_pangram(sentence):
    # Create a dictionary to store letters and their counts
    letters = dict()
    # Iterate over individual chars in the lowercase sentence
    for char in sentence.lower():
        # Test that the char is indeed an alphabet letter
        if char.isalpha():
            # If yes: update char count by 1 (if char in dict) or add char to dict
            letters[char] = letters.get(char, 0) + 1
    # Compare length of the dictionary to 26 (size of alphabet)
    # If length is 26 - every letter is present at least once --> return True
    # Else will mean that one ore more letters were not present in the sentence --> False
    return len(letters) == 26
        
    
