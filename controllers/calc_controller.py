from services.solution_service_abc import SolutionServiceABC

class CalculationController:
    def __init__(self, _solutionServiceABC: SolutionServiceABC):
        self._solutionServiceABC = _solutionServiceABC
    
    def handle_args(self,args):
        if(args[0].isdigit()):
            return args[0]
        else:
            result = self.__solve_expressions(args[0])
            return result

    def __solve_expressions(self, args):

        return self._solutionServiceABC.solve_expressions(args)