import unittest
from services.solution_service import SolutionService
from controllers.calc_controller import CalculationController
from services.solution_service import SolutionService

# run python3 -m unittest tests/test_solution_service.py from the source folder

class SolutionServiceTester(unittest.TestCase):

	def test_solve_expressions_digit(self):
		arg = ['123456']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = int(calcController.handle_args(arg))
		self.assertEqual(123456,result, "integer argument test")
			
	def test_solve_expressions_1(self):
		arg = ['(add 5 6)']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(11,result, "basic single digit add")

	def test_solve_expressions_2(self):
		arg = ['(multiply 5 6)']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(30,result,"basic single digit multiply")

	def test_solve_expressions_3(self):
		arg = ['(add 10 456)']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(466,result,"basic multiple digit add")

	def test_solve_expressions_4(self):
		arg = ['(multiply 10 50)']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(500,result,"basic multiple digit multiply")

	def test_solve_expressions_5(self):
		arg = ['(add (multiply 12 10) 5)']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(125,result,"first expression having function")

	def test_solve_expressions_6(self):
		arg = ['(add 20 (multiply 3 40))']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(140,result,"second expression having function")

	def test_solve_expressions_7(self):
		arg = ['(add (add 45 3) (multiply 3 40))']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(168,result,"both expressions having function")

	def test_solve_expressions_8(self):
		arg = ['(multiply 2 (add (multiply 2 3) 8))']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(28,result, "multiple nested expression 1")

	def test_solve_expressions_9(self):
		arg = ['(multiply 2 (add (multiply 2 (add 1 2)) (multiply (add 1 2) 5)))']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(42,result, "multiple nested expression 2")

	def test_solve_expressions_10(self):
		arg = ['(multiply 2 (add (multiply 2 (add 1 2) (add 3 2)) (multiply (add 1 2) 5)))']
		expressionSolver = SolutionService()
		calcController = CalculationController(expressionSolver)
		result = calcController.handle_args(arg)
		self.assertEqual(90,result, "multiple nested and number of expressions")


if __name__=='__main__':
	unittest.main()





