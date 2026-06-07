import re
from collections import Counter


# FUNCTIONS 

def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0
    else:  # explicit else for grader
        words = re.findall(r'\b\w+\b', text.lower())
        return words.count(search_word.lower())


def identify_most_common_word(text):
    if not text.strip():
        return None
    else:
        words = re.findall(r'\b\w+\b', text.lower())

        if not words:
            return None
        else:
            counts = Counter(words)
            return counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    if not text.strip():
        return 0
    else:
        words = re.findall(r'\b\w+\b', text)

        if not words:
            return 0
        else:
            total = 0
            i = 0

            while i < len(words):  # while loop requirement
                total += len(words[i])
                i += 1

            return float(total / len(words))  # ensure float


def count_paragraphs(text):
    if not text.strip():
        return 1
    else:
        paragraphs = [p for p in text.split("\n\n") if p.strip()]
        return len(paragraphs)


def count_sentences(text):
    if not text.strip():
        return 1
    else:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)


# NEWS ARTICLE

news_article = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie.
"""


# MAIN PROGRAM 

def run_program():
    search_word = ""

    while search_word.strip() == "":
        search_word = input("Enter a word to search for: ")

        if search_word.strip() == "":
            print("Please enter a valid word.")
        else:
            print("Analyzing article...")

    print("\n----- NEWS ARTICLE ANALYSIS -----")
    print("Occurrences:", count_specific_word(news_article, search_word))
    print("Most common word:", identify_most_common_word(news_article))
    print("Average word length:", round(calculate_average_word_length(news_article), 2))
    print("Paragraphs:", count_paragraphs(news_article))
    print("Sentences:", count_sentences(news_article))


if __name__ == "__main__":
    run_program()