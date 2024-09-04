# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return f.readlines()

def count_words(sentences):
    total_words = 0
    for sentence in sentences:
        words = sentence.split()
        total_words += len(words)
    return total_words

def most_frequent_word(sentences):
    
    word_count = {}

    for sentence in sentences:
        words = sentence.lower().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    most_frequent = ""
    highest_count = 0
    
    for word in word_count:
        if word_count[word] > highest_count:
            most_frequent = word
            highest_count = word_count[word]

    return most_frequent

def average_word_length(sentences):
    total_length = 0
    total_words = 0
    
    for sentence in sentences:
        words = sentence.split()
        total_words += len(words)
        for word in words:
            total_length += len(word)
    
    if total_words > 0:
        average_length = total_length / total_words
    else:
        average_length = 0
    
    return average_length

def main():
    
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt") # Här har du nu en lista av strängar från den inlästa filen.

    total_words = count_words(sentences)
    print(f"Antal ord: {total_words}")

    common_word = most_frequent_word(sentences)
    print(f"Mest frekventa ord: {common_word}")

    avg_length = average_word_length(sentences)
    print(f"Genomsnittlig ordlängd: {avg_length:.2f}")

if __name__ == "__main__":
    main()