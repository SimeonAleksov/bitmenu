class CaseConverter:
    @staticmethod
    def camel_case_to_snake_case(field):
        output = ''
        if field[0].isupper():
            field = field.replace(field[0], field[0].lower())
        for letter in field:
            if letter.upper() == letter and letter != '_':
                output += '_' + letter.lower()
            else:
                output += letter
        return output

    @staticmethod
    def snake_case_to_camel_case(field):
        output = ''
        next_case_upper = False
        for letter in field:
            if letter == '_':
                next_case_upper = True
            elif next_case_upper:
                output += letter.upper()
                next_case_upper = False
            else:
                output += letter
        return output
