import re


def parse(file_path: str):
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\b[a-zA-Z]+\b', text)

    return [word for word in words if len(word) <= 30]


def word_frequency(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def main(file_path: str):
    words = parse(file_path)
    word_count = word_frequency(words)

    print("Words with their frequency:")
    for word, count in word_count.items():
        print(f"{word} - {count}")


if __name__ == '__main__':
    main('text.txt')
