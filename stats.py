def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
	return d["num"]

def chars_dict_to_list(chars_dict):
    result = []  # step 1

    for ch in chars_dict:  # step 2
        count = chars_dict[ch]  # step 3a

        # step 3b + 3c: make a dict and append it
        small_dict = {"char": ch, "num": count}
        result.append(small_dict)

    result.sort(reverse=True, key=sort_on)
    return(result)
