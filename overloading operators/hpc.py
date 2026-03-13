import string


class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        num = self.number
        roman_numeral = ""

        for value, symbol in roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral
object_1 = IntegerToRoman(67676).convert()
print("your roman numeral is :" , object_1)