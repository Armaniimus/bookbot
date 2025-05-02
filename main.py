from stats import get_word_count, count_chars, sort_dictionary
import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	path = sys.argv[1]

	text = get_book_text(path)
	
	char_counts = count_chars(text)
	sorted_dictionary = sort_dictionary(char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {get_word_count(text)} total words")
	print("--------- Character Count -------")

	for i in sorted_dictionary:
		key=i["char"]
		count=i["count"]
		print(f"{key}: {count}")

	print("============= END ===============")

main()

