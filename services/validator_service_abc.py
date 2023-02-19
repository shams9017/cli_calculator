import abc

class ValidatorServiceABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate_argument(self, args):
        pass