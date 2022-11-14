import re


def find_match_lines(file_name: str):
    try:
        with open(file_name) as file:
            lines = file.read().splitlines()
            for line in lines[:-1]:
                get_matched_line(line, lines[-1])
    except FileNotFoundError:
        error_msg = 'File not found error'
        print(error_msg)
        return error_msg


def get_matched_line(line, search_term):
    words_re = re.compile(r"([a-zÀ-ÿ]+)", re.IGNORECASE)
    list_words = words_re.findall(line)
    found = list(filter(lambda word: re.search(search_term, word), list_words))
    if found:
        found_line = f"[{' '.join(list_words)}]"
        print(found_line)
        return found_line
    else:
        return 'sentence Not Match'


if __name__ == "__main__":
    assert get_matched_line('some sentence with ee', 'ee') == '[some sentence with ee]'
    assert get_matched_line('some sentence without match', 'ee') == 'sentence Not Match'
    assert find_match_lines("file not found.txt") == 'File not found error'
