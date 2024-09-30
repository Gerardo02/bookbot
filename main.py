def read_text():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    characters = {}
    for t in text:
        if characters.get(t) == None:
            characters[t] = 1
        else:
            characters[t] += 1

    return characters

def construct_report(dict):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report = report + f"{count_words(read_text())} words found in the document\n\n"

    for key in dict.keys():
        report = report + f"The '{key}' character was found {dict.get(key)} times \n"

    report = report + "--- End report ---"
    return report



if __name__ == "__main__":
    # print(count_words(read_text()))
    # print(count_characters(read_text()))
    print(construct_report(count_characters(read_text())))
