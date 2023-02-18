import abc

class SolutionServiceABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def solve_expressions(self, args):
        pass
