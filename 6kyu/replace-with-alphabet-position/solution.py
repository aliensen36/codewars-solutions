text = "The sunset sets at twelve o' clock."

def alphabet_position(text):
    return " ".join(str(ord(char) - ord('a') + 1)
                     for char in text.lower()
                     if char in "abcdefghijklmnopqrstuvwxyz")

if __name__ == "__main__":
    print(alphabet_position(text))

