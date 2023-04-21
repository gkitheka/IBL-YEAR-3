def count(s):
    # Split the text by whitespace
    words = s.split()
    
    # Initialize a counter for the number of "um"s found
    um_count = 0
    
    # Loop over the words in the text
    for word in words:
        # Remove any punctuation from the word
        word = word.strip(",.?!-\"\'")
        # If the word is "um" (case-insensitive), increment the counter
        if word.lower() == "um":
            um_count += 1
    
    return um_count



def main():
    text = input("Text: ")
    um_count = count(text)
    print(f"Number of 'um's found: {um_count}")




