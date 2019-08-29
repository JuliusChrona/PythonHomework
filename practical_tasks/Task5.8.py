class NumberConventer():
    CONV_TABLE = tuple(zip([1000, 900, 500, 400, 100, 90,
                           50, 40, 10, 9, 5, 4, 1],
                           ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL',
                            'X', 'IX', 'V', 'IV', 'I']))

    @staticmethod
    def convert_from_arab(arab_number: int):
        if arab_number <= 0:
            return 0 if arab_number == 0 else "Number < 0"
        result = ''
        for arab, roman in NumberConventer.CONV_TABLE:
            while arab_number >= arab:
                result += roman
                arab_number -= arab
        return result

    @staticmethod
    def convert_from_roman(roman_number: str):
        result = 0
        for arab, roman in NumberConventer.CONV_TABLE:
            while roman_number.startswith(roman):
                result += arab
                roman_number = roman_number[len(roman):]
        return result


converter = NumberConventer()
integer = converter.convert_from_roman('MCCXLI')
print(integer)
roman_numeral = converter.convert_from_arab(1543)
print(roman_numeral)
