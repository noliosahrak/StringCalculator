class StringCalculator:
    @staticmethod
    def add(calc_input):
        if not calc_input:
            return 0
        else:
            numbers = calc_input.split(",")
            result = 0

            for number in numbers:
                result += int(number)
            return result
