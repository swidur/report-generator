class FileTooBigError(Exception):
    # Exception is raised when trying to open file bigger than allowed
    def __init__(self, message, foo, *args):
        self.message = message
        self.foo = foo
        super(FileTooBigError, self).__init__(message, foo, *args)

