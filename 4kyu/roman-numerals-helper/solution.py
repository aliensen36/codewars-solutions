class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]
        parts = []
        for value, symbol in pairs:
            while val >= value:
                parts.append(symbol)
                val -= value
        return ''.join(parts)

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman_map = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,
        }
        total = 0
        i = 0
        while i < len(roman_num):
            if roman_num[i] in roman_map:
                total += roman_map[roman_num[i]]
                i += 1
        return total

print(RomanNumerals.to_roman(13))
print(RomanNumerals.from_roman('MDCLXVI'))