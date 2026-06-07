import re

# 1. Count specific word
def count_specific_word(text, word):
    words = text.lower().split()
    return words.count(word.lower())


# 2. Most common word
def identify_most_common_word(text):
    if text.strip() == "":
        return None

    words = text.lower().split()
    most_common = words[0]

    for w in words:   # FOR LOOP ✅
        if words.count(w) > words.count(most_common):
            most_common = w

    return most_common


# 3. Average word length (FIXED)
def calculate_average_word_length(text):
    if text.strip() == "":
        return 0

    words = re.findall(r'\b\w+\b', text)

    total = 0
    i = 0

    while i < len(words):   # WHILE LOOP ✅
        total += len(words[i])
        i += 1

    return float(total / len(words))   # must return FLOAT ✅


# 4. Paragraphs (FIXED)
def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip() != ""]
    return len(paragraphs)


# 5. Sentences (FIXED)
def count_sentences(text):
    if text.strip() == "":
        return 1

    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip() != ""]
    return len(sentences)


# --- MAIN ---
text = input("Enter text: ")
word = input("Enter word to count: ")

print("Word count:", count_specific_word(text, word))
print("Most common word:", identify_most_common_word(text))
print("Average word length:", calculate_average_word_length(text))
print("Paragraphs:", count_paragraphs(text))
print("Sentences:", count_sentences(text))