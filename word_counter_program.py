import re
from collections import Counter

def count_unique_words(input_file, output_file):
    # Read the input file and extract the words
    with open(input_file, 'r') as file:
        text = file.read().lower()

    # Use regular expression to extract alphanumeric words
    words = re.findall(r'\b\w+\b', text)

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Write the results to the output file
    with open(output_file, 'w') as file:
        for word, count in sorted_word_counts:
            file.write(f"{word}: {count}\n")

    print("Word count completed and saved to", output_file)

# Example usage
input_file = 'input.txt'  # Replace with your input file name
output_file = 'word_count.txt'  # Replace with the desired output file name

count_unique_words(input_file, output_file)
