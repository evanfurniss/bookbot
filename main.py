def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_arr = file_contents.split()
        occurrences = count_char_occurrences(words_arr)

def count_char_occurrences(arr):
    char_occurrences = {}

    # split each arr index to:
    # First, remove any whitespace (there should not be any)
    # Then, split each index (str) to an array of chars
    # Then, initializes the key in char_occurrences object if it does not exist set to 1 occurrence, or +1 to the occurrence
    # Finally, once arr finishes looping, return char_occurrences

    return char_occurrences
    

main()