from StringCalculator import StringCalculator


def test_should_be_zero_when_empty():
    calculator = StringCalculator()
    assert calculator.add("") == 0


def test_should_return_number_when_number_given():
    calculator = StringCalculator()
    assert calculator.add("2") == 2


def test_should_return_sum_of_numbers_when_more_numbers_given():
    calculator = StringCalculator()
    assert calculator.add("2,5,8,9,10") == 34
