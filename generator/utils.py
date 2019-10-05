from .errors import ParameterError


def check_if_char(param):
    if not isinstance(param, str):
        raise ParameterError(
            msg="Parameter is not a string", desc=f"It is {type(param)}"
        )
    if len(param) != 1:
        raise ParameterError(msg="Parameter is not a single sign")


def check_if_word(param):
    if not isinstance(param, str):
        raise ParameterError(
            msg="Parameter is not a string", desc=f"It is {type(param)}"
        )


def check_if_list_of_chars(param):
    if not isinstance(param, list):
        raise ParameterError(
            msg="Parameter is not a list", desc=f"It is {type(param)}"
        )
    for value in param:
        if not isinstance(value, str):
            raise ParameterError(
                msg="Value in list is not a string",
                desc=f"It is {type(value)}"
            )
        if len(value) != 1:
            raise ParameterError(msg="Value in list is not a single sign")


def check_if_matrix_of_numbers(param):
    if not isinstance(param, list):
        raise ParameterError(
            msg="Parameter is not a list", desc=f"It is {type(param)}"
        )
    for value in param:
        if not isinstance(param, list):
            raise ParameterError(
                msg="Element of list is not a list",
                desc=f"It is {type(param)}"
            )
    for value in param:
        for element in value:
            if not isinstance(element, (int, float)):
                raise ParameterError(
                    msg="Value in list is not a int nor float",
                    desc=f"It is {type(element)}"
                )