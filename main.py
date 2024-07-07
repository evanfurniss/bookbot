def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_arr = file_contents.split()
        num_words = len(words_arr)
        occurrences = count_char_occurrences(words_arr)
        chars_list = list_char_occurrences(occurrences)
        report = get_report(num_words, chars_list)
        print(report)

def count_char_occurrences(arr):
    char_occurrences = {}
    
    for str in arr:
        lower = str.lower()
        for k in lower:
            if k in char_occurrences:
                char_occurrences[k] += 1
            else:
                char_occurrences[k] = 1
    
    return char_occurrences

def get_report(num_words, chars_list):
    str = f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n\n"
    for dict in chars_list:
        str += f"The '{dict['char']}' character was found {dict['num']} times\n"
    str += "--- End report ---"
    return str

def sort_chars(dict):
    return dict["num"]

def list_char_occurrences(occurrences):
    list_chars = []

    for k,v in occurrences.items():
        if k.isalpha():
            list_chars.append({"char": k,"num": v})
    
    list_chars.sort(reverse=True, key=sort_chars)
    
    return list_chars

main()