from collections import Counter


def duplicate_count(text):
    return sum(1 for key, value in Counter(text.lower()).items() if value > 1)


if __name__ == "__main__":
    print(duplicate_count("abcde"))
    print(duplicate_count("aabbcde"))
    print(duplicate_count("aabBcde"))
    print(duplicate_count("indivisibility"))
    print(duplicate_count("Indivisibilities"))
    print(duplicate_count("aA11"))
    print(duplicate_count("ABBA"))
