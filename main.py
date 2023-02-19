import sys
from services.solution_service import SolutionService
from controllers.calc_controller import CalculationController

def main():
    args = sys.argv
    args = args[1:]  

    expressionSolver = SolutionService()
    calcController = CalculationController(expressionSolver)

    result = calcController.handle_args(args)

    if(result != None):
        print(result)


if __name__ == "__main__":
    main()