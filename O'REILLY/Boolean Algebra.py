# https://py.checkio.org/en/mission/boolean-algebra/


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0]:
        if x == y:
            if x == 1:
                return 1
            else:
                return 0
        else:
            return 0
    if operation == OPERATION_NAMES[1]:
        if x == 1 or y == 1:
            return 1
        else:
            return 0
    if operation == OPERATION_NAMES[2]:
        if x == 1 and y == 0:
            return 0
        else:
            return 1
    if operation == OPERATION_NAMES[3]:
        if x == y:
            return 0
        else:
            return 1
    if operation == OPERATION_NAMES[4]:
        if x == y:
            return 1
        else:
            return 0
