__error: str


def required(error: str):
    global __error
    __error = error
    return __required


def __required(text: str):
    if (text.strip() == ''):
        return __error
