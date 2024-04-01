class MethodError(Exception):
    def __init__(self, error="Request Method Error"):
        self.error = error

    def __str__(self):
        return repr(self.error)
