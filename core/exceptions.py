class MethodError(Exception):
    def __init__(self, error: str = "Request Method Error"):
        self.error = error

    def __str__(self):
        return repr(self.error)


class ValidatorError(Exception):
    def __init__(self, error: str = "Validator Error"):
        self.error = error

    def __str__(self):
        return repr(self.error)


class ExporterError(Exception):
    def __init__(self, error: str = "Exporter Error"):
        self.error = error

    def __str__(self):
        return repr(self.error)
