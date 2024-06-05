def print_upper_words(words, letters):
    """Takes a list of words and prints out each individual word on a new
    line in all upper_case letters
    """
        
    for word in words:
        for letter in letters:
            if word[0] == letter.upper() or word[0] == letter.lower():
                print( f"\n {word.upper()}")