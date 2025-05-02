def get_word_count(text):
	return len(text.split())

def count_chars(text):
	char_counts={}
	text = text.lower()
	for char in text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1

	return char_counts

def sort_dictionary(dictionary): 
	list = []
	for key in dictionary:
		char_dict = {"char": key, "count": dictionary[key]}
		list.append(char_dict)

	list.sort(reverse=True, key=sort_on)
	return list

def sort_on(dict):
    return dict["count"]