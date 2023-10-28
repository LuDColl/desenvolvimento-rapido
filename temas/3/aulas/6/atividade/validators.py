_error: str


def required(error: str):
    global _error
    _error = error
    return _required


def _required(text: str) -> str:
    if (text.strip() == ''):
        return _error
