import sys

def getCiphterte(keyword, plain_text):
    dictionary = []
    cipherte = list()
    for character in keyword:
        if character not in dictionary:
            dictionary.append(character)
            cipherte.append(character)
    for character in plain_text:
        if character not in dictionary:
            dictionary.append(character)
            cipherte.append(character)
    return "".join(cipherte)


def encode(text, mapper):
    result = [ mapper[character] if character in mapper.keys() else character for character in text.lower() ]
    result = [ result[i].upper() if text[i].isupper() else result[i] for i in range(0, len(text)) ]
    return "".join(result)


def get_file_name():
    n = len(sys.argv)
    if n == 1:
        raise Exception(f"Please specify file name as first parameter.")
    
    file_name = str(sys.argv[1])
    file = open(file_name, "r")

    if file is None:
        raise Exception(f"Couldn't open {file_name} file")
    return file


if __name__ == "__main__":
    file = get_file_name()
    test_text = file.read()

    cipher_keyword = input("Please enter a keyword for the mixed cipher: ")
    cipher_keyword = cipher_keyword.lower()

    plain_text = "abcdefghijklmnopqrstuvwxyz"
    cipherte = getCiphterte(cipher_keyword, plain_text)

    print(f"Plaintext: {plain_text}")
    print(f"Cipherte: {cipherte}")

    mapper = dict([ (plain_text[i],cipherte[i]) for i in range(0, len(plain_text)) ])

    encoded_text = encode(test_text, mapper)
    print("Result: ", encoded_text)