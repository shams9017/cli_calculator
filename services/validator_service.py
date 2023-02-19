# This is used to validate if the input argument is malformed
# incomplete at this time
from validator_service_abc import ValidatorServiceABC

class ValidatorService(ValidatorServiceABC):
    def validate_argument(self, args):
        pass