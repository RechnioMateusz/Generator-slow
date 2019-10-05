class DependenciesMatrixError(Exception):
    def __init__(self, msg, desc=None):
        super().__init__(self, msg)
        self.msg = msg
        self.desc = desc

    def __str__(self):
        return f"DependenciesMatrixError: {self.msg}\nDescription: {self.desc}"


class PropabilityMatrixError(Exception):
    def __init__(self, msg, desc=None):
        super().__init__(self, msg)
        self.msg = msg
        self.desc = desc

    def __str__(self):
        return f"PropabilityMatrixError: {self.msg}\nDescription: {self.desc}"


class WordGenMatrixError(Exception):
    def __init__(self, msg, desc=None):
        super().__init__(self, msg)
        self.msg = msg
        self.desc = desc

    def __str__(self):
        return f"WordGenMatrixError: {self.msg}\nDescription: {self.desc}"


class ParameterError(Exception):
    def __init__(self, msg, desc=None):
        super().__init__(self, msg)
        self.msg = msg
        self.desc = desc

    def __str__(self):
        return f"ParameterError: {self.msg}\nDescription: {self.desc}"
