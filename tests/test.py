from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_success(self):
        assert self.calc.division(self, 20, 2) == 10

    def test_subtraction_calculate_success(self):
        assert self.calc.subtraction(self, 8, 5) == 3

    def test_adding_calculate_success(self):
        assert self.calc.adding(self, 5, 3) == 8
