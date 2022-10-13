class KeyNotInJSON(Exception):

    def __init__(self, key) -> None:
        self.key = key
        if self.key is None or len(self.key) == 0:
            self.message = 'Key is missing in dictionary'
        else:
            self.message = f'Key <{self.key}> is missing in dictionary'
        super().__init__(self.message)

class InvalidParameter(Exception):

    pass